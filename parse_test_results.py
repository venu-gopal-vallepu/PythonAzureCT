from junitparser import JUnitXml
import re

# Load the JUnit XML file
xml = JUnitXml.fromfile('test-results.xml')

# Regular expression pattern to match '__' followed by any number (which represents the test case ID)
pattern = re.compile(r"__(\d+)$")

# Iterate through each test suite and case
for suite in xml:
    for case in suite:
        match = pattern.search(case.name)
        if match:
            test_case_id = match.group(1)
            # Initialize outcome
            outcome = 'Pass'
            # Check if case.result is a list
            if isinstance(case.result, list):
                # Iterate through the results
                for result in case.result:
                    if result._tag == 'failure':
                        outcome = 'Fail'
                        break  # No need to check other results if one has failed
                    elif result._tag == 'skipped':
                        outcome = 'Skipped'
                        break  # Consider skipped if any result is skipped
            elif case.result:  # case.result is not a list, but a single result object
                if case.result._tag == 'failure':
                    outcome = 'Fail'
                elif case.result._tag == 'skipped':
                    outcome = 'Skipped'
            # Use the test_case_id and outcome to update Azure DevOps