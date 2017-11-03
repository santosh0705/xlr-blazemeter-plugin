# Preface #

This document describes the functionality provided by the xlr-blazemeter-plugin.

See the **[XL Release Reference Manual](https://docs.xebialabs.com/xl-release/)** for background information on XL Release and release concepts.

# Overview #

The xlr-blazemeter-plugin is a XL Release plugin provides a task which run [Blazemeter](https://www.blazemeter.com/) application tests. This plugin start a test on Blazemeter, monitor the progress and complete the task when the test ends.

## Types ##

You can pass all valid Jmeter parameter to task. It will be modify the Jmeter parameters in the test project before it start the test.
