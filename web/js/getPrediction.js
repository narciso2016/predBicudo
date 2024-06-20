        function getPrediction( tar, ur, ppt, vv, rs, evt, torv, mes) {


              if (window.XMLHttpRequest) { // FireFox, Mozilla, Safari,...
                  xmlHttpObject = new XMLHttpRequest();
                  if (xmlHttpObject.overrideMimeType) {
                     xmlHttpObject.overrideMimeType('text/xml');
                  }
              } else if (window.ActiveXObject) { // Internet Explorer
                    try {
                             xmlHttpObject = new ActiveXObject("Msxml2.XMLHTTP"); // Internet Explorer 5.5+
                        } catch (e) {
                                      try {
                                             xmlHttpObject = new ActiveXObject("Microsoft.XMLHTTP"); //Internet Explorer 5.5-
                                          } catch (e) {}
                                    }
               }
              if (!xmlHttpObject) {
                        alert('Impossivel criar instancia do objeto XMLHttpResquest.');
                        return false;
              }

              xmlHttpObject.onreadystatechange = predicao; //especifica a funcao JAVASCRIPT que recebera o resultado
              xmlHttpObject.open('GET','predicao.php?tar=' + tar + '&ur=' + ur + '&ppt=' + ppt + '&vv=' + vv + '&torv=' + torv + '&rs=' + rs + '&evt=' + evt + '&mes=' + mes);
              xmlHttpObject.send(); // envia par.metros ao servidor se for pelo metodo POST
              return false;



        }
        function predicao() {
        
           if (xmlHttpObject.readyState == 4) {
           
                if (xmlHttpObject.status == 200) {

                    newTexto = xmlHttpObject.responseText;
                    j = newTexto.indexOf("<pred>");
                    s = "<pred>".length;
                    i = newTexto.length;
                    newTexto2 = "";
                    for(k= j + s; k < i; k++)
                      newTexto2 = newTexto2 + newTexto.charAt(k);
                    newTexto2 = newTexto2 + "";
                    newTexto3 = "";
                    j = newTexto2.indexOf("</pred>");
                    for(k= 0; k < j; k++)
                      newTexto3 = newTexto3 + newTexto2.charAt(k);
                    newTexto3 = newTexto3 + "";
                    newTexto = newTexto3;

                    if(newTexto.length > 3 ) {

                             results = newTexto.split(";");
                             alert('Probabilidade de aparecimento de bicudo: ' + results);

                    }
                    else {

                                alert('O sistema nao retornou resultado. Erro inesperado.');
                         }

                } 
                else {
                        alert('Problema na requisicao!');
                }

           }
           return true;
        }
