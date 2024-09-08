#!/usr/bin/env python3
# DESCRIPTION: Verilator: Verilog Test driver/expect definition
#
# Copyright 2024 by Wilson Snyder. This program is free software; you
# can redistribute it and/or modify it under the terms of either the GNU
# Lesser General Public License Version 3 or the Perl Artistic License
# Version 2.0.
# SPDX-License-Identifier: LGPL-3.0-only OR Artistic-2.0

import vltest_bootstrap

test.scenarios('vlt')
test.top_filename = "t/t_class_virtual.v"

# This test makes randomly named .cpp/.h files, which tend to collect, so remove them first
for filename in (glob.glob(test.obj_dir + "/*_PS*.cpp") + glob.glob(test.obj_dir + "/*_PS*.h") +
                 glob.glob(test.obj_dir + "/*.d")):
    test.unlink_ok(filename)

test.compile(verilator_flags2=["--protect-ids", "--protect-key SECRET_KEY"])

test.execute()

test.passes()
