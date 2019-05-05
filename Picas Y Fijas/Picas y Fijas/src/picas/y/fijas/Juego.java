/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package picas.y.fijas;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Objects;
import java.util.Random;
import java.util.Scanner;


/**
 *
 * @author DELL
 */
public class Juego {
    Random random = new Random();
    private final int[] numeros;
    private ArrayList clave = new ArrayList();
    
    public Juego(){
        this.numeros = new int[]{0,1,2,3,4,5,6,7,8,9};
    }
    
//  Define un codigo de n cifras no repetidas al azar
    private ArrayList crearCod(int n){
        ArrayList codigo = new ArrayList();
        for(int i=0; i<n; i++){
            int num_elegido = numeros[random.nextInt(numeros.length)];
            while(codigo.contains(num_elegido)){
                num_elegido = numeros[random.nextInt(numeros.length)];
            }
            codigo.add(num_elegido);
        }
        return codigo;
    }
    
//  Escoje una opción random de una lista de iteraciones
    private ArrayList elejirProp(ArrayList<ArrayList> listado){
        int temp = random.nextInt(listado.size());
        return listado.get(temp);
    }
    
//    #Crea lista con todas las iteraciones de n cifras en numeros()
    private ArrayList<ArrayList> crearComb(int n){
        ArrayList num = new ArrayList();
        for (int x:numeros) {
            num.add(x);
        }
        return choose(num, n);
    }
    
    private int[] comprobar(ArrayList codigo, ArrayList prop){
        int[] pyf = new int[]{0,0};
        for (int i = 0; i < codigo.size(); i++){
            if(((Integer)prop.get(i)).equals((Integer)codigo.get(i))){
                pyf[1] ++;
            } else if(codigo.contains(prop.get(i))){
                pyf[0] ++;
            }
        }
        return pyf;
    }
    
    public void jugar1(){
        clave = this.crearCod(4);
        System.out.println(clave);
        int intentos = 0;
        int[] pyf = new int[]{0,0};
        String str = "";
        while(pyf[1] != clave.size()){
            System.out.printf("Escoja una cifra de %d cifras no repetidas:\t", clave.size());
            Scanner scan = new Scanner(System.in);
            str = scan.next();
            
            if(str.equals("xxxx")) break;
            
            ArrayList prop = new ArrayList();
            char[] a = str.toCharArray();
            for(char c:a){
                    prop.add(Character.getNumericValue(c));
            }
            
            pyf = comprobar(clave,prop);
            intentos++;
            System.out.printf("Tu propuesta %s tiene %d picas y %d fijas\n\n", str, pyf[0], pyf[1]);
        }
//        if(str != "0000") System.out.printf("Felicidades. El número es:%s. Intentos:%i", Arrays.toString(clave.toArray()), intentos);
        if(str.equals("xxxx")){
            System.out.println("Decepcionante. El código es: " + clave);
        }
        else System.out.println("Felicidades. El número es:" + clave + ". Intentos: "+intentos);
    }
        
    public void jugar2(){
        
        System.out.println("Escoja un número de 4 cifras para que el computador lo adivine:\t");
        String str;
        Scanner scan = new Scanner(System.in);
        str = scan.next();
        if(clave.size()>0) clave.clear();
        char[] a = str.toCharArray();
        for(char c:a){
            clave.add(Character.getNumericValue(c));
        }
        this.adivinaPausado();
    }
    
    private void adivinaPausado(){
        ArrayList<ArrayList> listado = crearComb(4);
        int intentos = 0;
        int[] pyf = new int[]{0,0};
        ArrayList prop = new ArrayList();
        while(pyf[1] != 4){

            prop = this.elejirProp(listado);
            pyf = comprobar(clave,prop);

            System.out.printf("\nSi le da pereza pensar, el número de picas es %d y fijas es %d", pyf[0], pyf[1]);
            System.out.println("\nSupongo que el numero es " + prop);
            System.out.println("Cuantas picas obtuve, humano?");
            Scanner p = new Scanner(System.in);
            pyf[0] = Integer.parseInt(p.next());
            System.out.println("Cuantas fijas obtuve, humano?");
            Scanner f = new Scanner(System.in);
            pyf[1] = Integer.parseInt(f.next());

            ArrayList temp = new ArrayList();
            for (ArrayList i:listado) {
                int[] x = comprobar(i, prop);
                if((x[0] == pyf[0])&&(x[1] == pyf[1])){
                    temp.add(i);
                }
            }
            listado = temp;
            intentos++;
        }
        System.out.printf("\nTal parece que gané en "+intentos+" intentos, fácil.");
    }
        
    public void reglas(){
        System.out.println("\nPicas y fijas es un juego donde dos jugadores tratan de adivinar una clave secreta de 4 cifras \nno repetidas definida por su oponente, con las únicas pistas siendo el número de \npicas(cifras en la clave y en el lugar incorrecto) y fijas (cifras en la clave y \nen el lugar correcto). ");
        System.out.println("\nEjemplo: clave = 3701 \n1507 tiene 2 picas(1 y 7) y 1 fija(0)");
        System.out.println("\nEn la opción \"Usuario adivina\" el computador generará una clave y tú debes adivinarla.");
        System.out.println("\nEn la opción \"Computador adivina\" el computador adivinará una clave que tú te hayas inventado y \ndebes indicarle cuántas picas y fijas logró.");

    }
   
    //THE FOLLOWING METHODS i FOUND ON THE INTERNET. sADLY, i LOST THE SOURCE
    // IT WAS ORIGINALLY NAMED UNDER THE CLASS public class PermutationTest10
    
    // a is the original array
    // k is the number of elements in each permutation
    public static ArrayList<ArrayList> choose(ArrayList a, int k) {
        ArrayList<ArrayList> allPermutations = new ArrayList<ArrayList>();
        enumerate(a, a.size(), k, allPermutations);
        return allPermutations;
    }

  // a is the original array
    // n is the array size
    // k is the number of elements in each permutation
    // allPermutations is all different permutations
    private static void enumerate(ArrayList a, int n, int k, ArrayList<ArrayList> allPermutations) {
        if (k == 0) {
            ArrayList singlePermutation = new ArrayList();
            for (int i = n; i < a.size(); i++){
                singlePermutation.add(a.get(i));
            }
            allPermutations.add(singlePermutation);
            return;
        }

      for (int i = 0; i < n; i++) {
            swap(a, i, n-1);
            enumerate(a, n-1, k-1, allPermutations);
            swap(a, i, n-1);
        }
    }  

  // helper function that swaps a.get(i) and a.get(j)
    public static void swap(ArrayList a, int i, int j) {
        Integer temp = (Integer)a.get(i);
        a.set(i, a.get(j));
        a.set(j, temp);
    }


}