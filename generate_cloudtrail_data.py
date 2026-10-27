#!/usr/bin/env python3
"""
Generates continuous AWS API activity to populate CloudTrail logs.
Runs in a loop, making read-only calls across EC2, S3, IAM, and STS.
Kill with Ctrl+C when done.
"""

import boto3
import time
import random
import logging
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(message)s",
    datefmt="%H:%M:%S"
)
log = logging.getLogger()

# How long to wait between bursts (seconds)
INTERVAL = 60  # adjust as needed

def run_ec2(session):
    ec2 = session.client("ec2")
    ec2.describe_instances()
    log.info("EC2: describe_instances")
    ec2.describe_security_groups()
    log.info("EC2: describe_security_groups")
    ec2.describe_vpcs()
    log.info("EC2: describe_vpcs")

def run_s3(session):
    s3 = session.client("s3")
    s3.list_buckets()
    log.info("S3: list_buckets")

def run_iam(session):
    iam = session.client("iam")
    iam.list_users()
    log.info("IAM: list_users")
    iam.list_roles()
    log.info("IAM: list_roles")
    iam.list_policies(Scope="Local")
    log.info("IAM: list_policies")

def run_sts(session):
    sts = session.client("sts")
    identity = sts.get_caller_identity()
    log.info(f"STS: get_caller_identity → {identity['Arn']}")

def burst(session):
    runners = [run_ec2, run_s3, run_iam, run_sts]
    random.shuffle(runners)  # vary the order each burst
    for fn in runners:
        try:
            fn(session)
        except Exception as e:
            log.warning(f"Skipped {fn.__name__}: {e}")

def main():
    session = boto3.Session()
    log.info("Starting CloudTrail activity generator. Press Ctrl+C to stop.")
    log.info(f"Burst interval: {INTERVAL}s\n")

    count = 0
    while True:
        count += 1
        log.info(f"--- Burst #{count} ---")
        burst(session)
        log.info(f"Done. Sleeping {INTERVAL}s...\n")
        time.sleep(INTERVAL)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nStopped.")
