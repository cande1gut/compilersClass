
public class Sintactico {

	public boolean verificar(String terminal) {
		// leer la siguiente entrada y comparar con terminal
		return true;
	}

	public boolean exigir(String terminal) {
		// leer borrando la siguiente entrada y comparar con terminal.
		return true;
	}

	public void mostrarError() {
		System.out.println("Error sintactico :(");
		System.exit(0);
	}

	// <program> ::= "class" "program" "{" <functions> <main function> "}"
	private void program() {
		if(this.exigir("class")) {
			if(this.exigir("program")) {
				if(this.exigir("{")) {
					this.functions();
					this.mainFunction();
					if(!this.exigir("}"))
						this.mostrarError();
				} else
					this.mostrarError();
			} else
				this.mostrarError();
		} else
			this.mostrarError();
	}

	// <functions> ::= <function> <functions prima> | lambda
	private void functions() {
		if(this.verificar("void")) {
			this.function();
			this.functionPrima();
		}
	}

	// <function> ::= "void" <name function> "("  ")" "{" <body> "}"
	private void function() {
		if(this.exigir("void")) {
			this.nameFunction();
			if(this.exigir("(")) {
				if(this.exigir(")")) {
					if(this.exigir("{")) {
						this.body();
						if(!exigir("}"))
							this.mostrarError();
					} else
						this.mostrarError();
				} else
					this.mostrarError();
			} else
				this.mostrarError();
		} else
			this.mostrarError();
	}

	// <functions prima> ::= <function> <functions prima> | lambda
	private void functionPrima() {
		if(this.verificar("void")) {
			this.function();
			this.functionPrima();
		}
	}

	// <main function> ::= "program" "(" ")" "{" <body> "}"
	private void mainFunction() {
		if(this.exigir("program")) {
			if(this.exigir("(")) {
				if(this.exigir(")")) {
					if(this.exigir("{")) {
						this.body();
						if(!this.exigir("}"))
							this.mostrarError();
					} else
						this.mostrarError();
				} else
					this.mostrarError();
			} else
				this.mostrarError();
		} else
			this.mostrarError();
	}

	// <body> ::= <expression> <body prima>
	private void body() {
		this.expression();
		this.bodyPrima();
	}

	// <body prima> ::= <expression> <body prima> | lambda
	private void bodyPrima() {
		if(this.verificar("if") || this.verificar("while") || this.verificar("iterate") || this.verificar("move") || this.verificar("turnLeft") || this.verificar("pickBeeper") || this.verificar("putBeeper") || this.verificar("end")) {
			// verificar tambien por una palabra como lo hayas hecho en customerFunction
			this.expression();
			this.bodyPrima();
		}
	}

	// <expression> ::= <call function> | <if expression> | <while expression> | <iterate expression>
	private void expression() {
		if(this.verificar("if")) {
			this.ifExpression();
		} else if(this.verificar("while")) {
			this.whileExpression();
		} else if(this.verificar("iterate")) {
			this.iterateExpression();
		} else {
			this.callFunction();
		}
	}

	// <if expression> ::= "if" "(" <condition> ")" "{" <body>  "}" <else>
	private void ifExpression() {
		if(this.exigir("if")) {
			if(this.exigir("(")) {
				this.condition();
				if(this.exigir(")")) {
					if(this.exigir("{")) {
						this.body();
						if(this.exigir("}")) {
							this.elseExpression();
						} else
							this.mostrarError();
					} else
						this.mostrarError();
				} else
					this.mostrarError();
			} else
				this.mostrarError();
		} else
			this.mostrarError();
	}

	// <else> ::= "else" "{" <body> "}"  | lambda
	private void elseExpression() {
		if(this.verificar("else")) {
			if(this.exigir("else")) {
				if(this.exigir("{")) {
					this.body();
					if(!this.exigir("}"))
						this.mostrarError();
				} else
					this.mostrarError();
			} else
				this.mostrarError();
		}
	}

	// <while> ::= "while" "(" <condition> ")" "{" <body> "}"
	private void whileExpression() {
		if(this.exigir("while")) {
			if(this.exigir("(")) {
				this.condition();
				if(this.exigir(")")) {
					if(this.exigir("{")) {
						this.body();
						if(!this.exigir("}"))
							this.mostrarError();
					} else
						this.mostrarError();
				} else
					this.mostrarError();
			} else
				this.mostrarError();
		} else
			this.mostrarError();
	}

	// <iterate expression> ::= "iterate" "(" <number> ")" "{" <body> "}"
	private void iterateExpression() {
		if(this.exigir("iterate")) {
			if(this.exigir("(")) {
				this.number();
				if(this.exigir(")")) {
					if(this.exigir("{")) {
						this.body();
						if(!this.exigir("}"))
							this.mostrarError();
					} else
						this.mostrarError();
				} else
					this.mostrarError();
			} else
				this.mostrarError();
		} else
			this.mostrarError();
	}

	// <number> ::= numero natural del 1 al 100
	private void number() {
		int i;
		for(i = 1; i <= 100; i++) {
			if(this.verificar(Integer.toString(i))) {
				this.exigir(Integer.toString(i));
				break;
			}
		}
		if(i == 101)
			this.mostrarError();
	}

	/* <condition> ::= "front-is-clear" | "left-is-clear" | "right-is-clear" |
  	"front-is-blocked" | "left-is-blocked" | "right-is-blocked" |
  	"next-to-a-beeper" | "not-next to a beeper" |
  	"facing-north" | "facing-south" | "facing-east" | "facing-west" |
  	"not-facing-north" | "not-facing-south" | "not-facing-east" | "not-facing-west" |
  	"any-beepers-in-beeper-bag" | "no-beepers-in-beeper-bag" */
	private void condition() {
		String [] conditions = {"front-is-clear", "left-is-clear", "right-is-clear",
			  	"front-is-blocked", "left-is-blocked", "right-is-blocked",
			  	"next-to-a-beeper", "not-next to a beeper",
			  	"facing-north", "facing-south", "facing-east", "facing-west",
			  	"not-facing-north", "not-facing-south", "not-facing-east", "not-facing-west",
			  	"any-beepers-in-beeper-bag", "no-beepers-in-beeper-bag"};
		int i;
		for(i = 0; i < conditions.length; i++) {
			if(this.verificar(conditions[i])) {
				this.exigir(conditions[i]);
				break;
			}
		}
		if(i == conditions.length)
			this.mostrarError();
	}

	// <call function> ::= <name function> "(" ")"
	private void callFunction() {
		this.nameFunction();
		if(this.exigir("(")) {
			if(!this.exigir(")"))
				this.mostrarError();
		} else
			this.mostrarError();
	}

	// <name function> ::= <official function> | <customer function>
	private void nameFunction() {
		if(this.verificar("move") || this.verificar("turnLeft") || this.verificar("pickBeeper") || this.verificar("putBeeper") || this.verificar("end")) {
			this.officialFunction();
		} else
			this.customerFunction();
	}

	// <official function> ::= "move" | "turnLeft" | "pickBeeper" | "putBeeper" | "end"
	private void officialFunction() {
		String [] officialFunctions = {"move", "turnLeft", "pickBeeper", "putBeeper", "end"};
		int i;
		for(i = 0; i < officialFunctions.length; i++) {
			if(this.verificar(officialFunctions[i])) {
				this.exigir(officialFunctions[i]);
				break;
			}
		}
		if(i == officialFunctions.length)
			this.mostrarError();
	}

	// <customer function> ::= palabra de mas de 2 caracteres y menos de 11
	private void customerFunction() {
		// verificar (y luego exigir) una palabra de mas de 2 caracteres y menos de 11
	}

}
