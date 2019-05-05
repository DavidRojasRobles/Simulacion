/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package picas.y.fijas;
import java.util.Iterator;
import java.util.ArrayList;
import java.util.Scanner;

/**
 *
 * @author DELL
 */
public class PicasYFijas{
    
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        System.out.println("Bienvenido a picas y Fijas!");
        String op;
        do{
            System.out.println("\n\n1. Usuario adivina \n2. Computador adivina \n3. Reglas \n4. Salir");
            Scanner scan = new Scanner(System.in);
            System.out.println("\nEscoja una opción:\t");
            op = scan.next();
            Juego juego = new Juego();
        
            switch(op){
                case "1":
                    juego.jugar1();
                    break;
                case "2":
                    juego.jugar2();
                    break;
                case "3":
                    juego.reglas();
                    break;
                case "4":
                    op = "salir";
                    break;
            }
        }while(op != "salir");
        
        
    }
    
}
