/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package calculadorapp;

import jme.Expresion;

/**
 *
 * @author paoloescamilla
 */
public class Funciones {
    
    public static String resolver_exp (String exp_string){   
    
        Expresion exp = new Expresion( exp_string );
     return exp.evaluar().toString();
    }
     
    
     public static String resolver_exp_bisec (String exp_bisec_string, String extremoinferior, String extremosuperior, String iteraciones){ 
     
     Expresion exp = new Expresion("sol_bisec("+exp_bisec_string+",x,"+extremoinferior+","+extremosuperior+")");
         System.out.println("sol_bisec("+exp_bisec_string+",x,"+extremoinferior+","+extremosuperior+")");
     return exp.evaluar().toString();
         
     }
      
     public static String resolver_exp_newton (String exp_newton_string, String derivada,String puntoinicial, String iteraciones, boolean especificar_derivada){
         Expresion exp = null;
         
         if (especificar_derivada){
              exp = new Expresion("sol_newton("+exp_newton_string+","+derivada+",x,"+puntoinicial+","+iteraciones+")");
             // exp.setVariable("x", variable);
             //sol_newton(x*ln(x)-1,ln(x)+1,x,1,100)"
             System.out.println("sol_newton("+exp_newton_string+","+derivada+",x,"+puntoinicial+","+iteraciones+")");

         } else{
              exp = new Expresion("newton("+exp_newton_string+",x,"+puntoinicial+", "+iteraciones+")");
              //exp.setVariable("x", variable);
              
         }
      
         return exp.evaluar().toString();
     }   
     
     
      
    
   public static String resolver_exp_sec (String exp_sec_string, String puntoinicial, String puntoinicial2){ 
        
        Expresion exp = new Expresion("sol_sec("+exp_sec_string+",x,"+puntoinicial+","+puntoinicial2+")");
         Expresion exp2 = new Expresion("sol_sec(x*ln(x)-1,x,-10,10)");
       System.out.println(exp2.evaluar());
        return exp.evaluar().toString();
    
    }
}