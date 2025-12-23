package laberinto;

import java.util.Scanner;

public class Laberinto {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		System.out.println("======== LABERINTO ========\n");
		System.out.println("- INSTRUCCIONES:");
		System.out.println("Teclas de movimiento (WASD) :");
		System.out.println("W -> moverse hacia arriba");
		System.out.println("A -> moverse hacia la izquierda");   
		System.out.println("S -> moverse hacia la derecha");
		System.out.println("D -> moverse hacia abajo\n");
		
		System.out.println("Debes conducir a Mickey (►) hacia la salida (▓)\n");
		
        char[][] laberinto = {
                {'⬛', '⬛', '⬛', '⬛', '⬛', '⬛'},
                {'⬛', '►', '⬜', '⬜', '⬜', '⬛'},
                {'⬛', '⬛', '⬛', '⬜', '⬛', '⬛'},
                {'⬛', '⬛', '⬜', '⬜', '⬜', '⬛'},
                {'⬛', '⬛', '⬜', '⬛', '⬛', '⬛'},
                {'⬛', '⬜', '⬜', '⬜', '▓', '⬛'},
                {'⬛', '⬛', '⬛', '⬛', '⬛', '⬛'}
        };
		
		int filaMickey = 1;
		int columnaMickey = 1;
		
		boolean condicion = false;
		
		do {	
			for(char[] fila : laberinto) {
				for(char c : fila) {
					System.out.print(c);
				}
				System.out.println();
			}
			
			System.out.println("\n¿A dónde quieres ir (WASD)?");
			String tecla = sc.nextLine();
			
			int nuevaFila = filaMickey;
			int nuevaColumna = columnaMickey; 

			if(tecla.equalsIgnoreCase("w")) {
				nuevaColumna--;
			}else if(tecla.equalsIgnoreCase("a")) {
				nuevaFila--;
			}else if(tecla.equalsIgnoreCase("s")) {
				nuevaColumna++;
			}else if(tecla.equalsIgnoreCase("d")) {
				nuevaFila++;
			}else {
				System.out.println("Tienes que introducir una de estas 4 teclas: 'W, A, S, D'.");
			}

			if(nuevaFila < 0 || nuevaFila >= laberinto.length ||
				nuevaColumna < 0 || nuevaColumna >= laberinto[0].length) {
					System.out.println("\nNo puedes salir del laberinto!");
					continue;
				}
			
			if(laberinto[nuevaColumna][nuevaFila] == '⬛') {
				System.out.println("\nEl muro te impide moverte");
			}else if(laberinto[nuevaColumna][nuevaFila] == '⬜'){
				laberinto[columnaMickey][filaMickey] = '⬜';
				laberinto[nuevaColumna][nuevaFila] = '►';
				filaMickey = nuevaFila;
				columnaMickey = nuevaColumna;
			}else if(laberinto[nuevaColumna][nuevaFila] == '▓'){
				System.out.println("\n¡¡¡Has logrado escapar del laberinto!!!");
				condicion = true;
			}

		} while (condicion != true);
		sc.close();
	}
}