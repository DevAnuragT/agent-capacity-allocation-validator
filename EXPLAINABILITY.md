# Decision and Reasoning

The result is overallocated when any resource total exceeds its capacity. Otherwise it is within_capacity and reports remaining capacity for every resource. The implementation returns structured findings so a reviewer can see how each result was derived.

# Inputs and Data Sources

The caller supplies a resource-to-capacity map and assignments with unique IDs, exact resource names, and nonnegative finite amounts. Resource names are case-sensitive and unknown references are rejected. The only data source is the caller-provided payload plus the checked-in rules and code; no network or private-file access is used.

# Known Limitations and Constraints

This arithmetic check cannot assess skill fit, scheduling conflicts, time zones, concurrency, or whether capacity estimates are realistic. It does not move, reject, or approve assignments. The result is a bounded pre-review aid and must not be presented as professional certification or an official HiDevs result.
