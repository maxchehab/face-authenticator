#!/bin/bash
echo $(gdbus call -e -d com.canonical.Unity -o /com/canonical/Unity/Session -m com.canonical.Unity.Session.IsLocked | grep -ioP "(true)|(false)")
