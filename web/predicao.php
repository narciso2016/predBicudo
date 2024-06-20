<?php

$tempAr = $_GET["tar"];
$umidRel = $_GET["ur"];
$precipt = $_GET["ppt"];
$velVento = $_GET["vv"];
$rs = $_GET["rs"];
$evt = $_GET["evt"];
$torv = $_GET["torv"];
$mes = $_GET["mes"];


   $mes1 = 0;    $mes2 = 0;  $mes3 = 0;
   $mes4 = 0;    $mes5 = 0;  $mes6 = 0;
   $mes7 = 0;    $mes8 = 0;  $mes9 = 0;
   $mes10 = 0;    $mes11 = 0;  $mes12 = 0;

   if($mes == 1)  $mes1 = 1;  
   else
      if($mes == 2)  $mes2 = 1; 
      else
        if($mes == 3)  $mes3 = 1; 
        else
          if($mes == 4)  $mes4 = 1; 
          else
            if($mes == 5)  $mes5 = 1; 
            else
              if($mes == 6)  $mes6 = 1; 
              else
                if($mes == 7)  $mes7 = 1; 
                else
                  if($mes == 8)  $mes8 = 1; 
                  else
                    if($mes == 9)  $mes9 = 1; 
                    else
                      if($mes == 10)  $mes10 = 1; 
                      else
                        if($mes == 11)  $mes11 = 1; 
                        else
                          if($mes == 12)  $mes12 = 1; 
 


    if ( $umidRel < 42.97 ){

      if($tempAr < 26.3) {
          echo "<pred>muito baixa</pred>";  
      }      
      else{
            if($mes10 < 0.5){

               if($mes9 < 0.5){
                               if($tempAr < 26.61)
                                                echo "<pred>muito baixa</pred>";
                               else
                                                echo "<pred>baixa</pred>";
               }                                 
               else{
                               if($tempAr < 29.08 ) 
                                                echo "<pred>muito baixa</pred>";
                               else 
                                      if( $precipt < 0.55) 
                                                echo "<pred>muito alta</pred>";                                         
                                      else      
                                                echo "<pred>muito baixa</pred>"; 
                   }
            }                                                      
            else
                echo "<pred>muito baixa</pred>";                 
      }
    }
    else {
           if($velVento < 2.34)
                  echo "<pred>muito baixa</pred>";         
           else {
                 if($umidRel < 53.06) {
                                         if( $velVento < 3.45) {
                                                echo "<pred>muito alta</pred>";    
                                         }                                      
                                         else {
                                                if($tempAr < 21.19)
                                                     echo "<pred>muito alta</pred>";
                                                else 
                                                     echo "<pred>muito baixa</pred>";  
                                         }                                                

                 }
                 else {
                        if($tempAr < 22.71)
                           echo "<pred>muito alta</pred>";
                        else
                           echo "<pred>muito baixa</pred>";    
                 }

           }                       
     }

    // Final de if ( $tempAr < 23.08 )


?>
