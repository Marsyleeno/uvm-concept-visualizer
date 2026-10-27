interface coffee_if(input logic clk);
  import coffee_pkg::*;
  size_e        size;
  logic         with_milk;
  logic         with_foam;
  coffee_type_e coffee_type;
endinterface