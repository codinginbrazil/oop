{
	Cálculo de área de um círculo
		* Pedir raio e circunferência
}

program areaCirculo;
var
	area : real;
	pi : real;
	raio : real;
begin
	pi := 3.1415;
	writeln('Informe o raio');
	readln(raio);
	
	area := pi*(raio*raio);
	writeln('A area:',area:3:2);
end.