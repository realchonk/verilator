// DESCRIPTION: Verilator: Verilog Test module
//
// This file ONLY is placed under the Creative Commons Public Domain, for
// any use, without warranty, 2024 by Wilson Snyder.
// SPDX-License-Identifier: CC0-1.0

virtual class Base;
    pure constraint raint;
endclass

class Cls extends Base;
   // Bad: Missing 'constraint raint'
endclass

module t;
endmodule
