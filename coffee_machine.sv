module coffee_machine(
  input logic clk,
  input coffee_pkg::size_e size,
  input logic with_milk,
  input logic with_foam,
  output coffee_pkg::coffee_type_e coffee_type
);
  import coffee_pkg::*;
  
  always_ff @(posedge clk) begin
    case ({size, with_milk, with_foam})
      3'b000: coffee_type <= ESPRESSO;
      3'b110: coffee_type <= LATTE;
      3'b111: coffee_type <= CAPPUCCINO;
      default: coffee_type <= NONE;
    endcase
  end
endmodule