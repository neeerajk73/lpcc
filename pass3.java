import java.io.*;

public class pass3 {
    public static void main(String[] args)throws Exception{
        FileReader fp=new FileReader("input.txt");
        BufferedReader bf=new BufferedReader(fp);
        int line_count=0,LC=0,symline=0,opline=0,litline=0;

        String [][] Symtable=new String[100][3];
        String [][] Optable=new String[100][3];
        String [][] Littable=new String[100][3];
        String line="";
        while((line=bf.readLine())!=null){
            String[] token=line.split("\t");
            if(line_count==0){
               LC=Integer.parseInt(token[1]);
               for(int i=0;i<token.length;i++){
                System.out.print(token[i]+"\t");
               }
               System.out.println("");
            }
            else{
                for(int i=0;i<token.length;i++){
                    System.out.print(token[i]+"\t");
                }
                System.out.println("");
            }
            if(!token[0].equals("")||token[1].equalsIgnoreCase("DS")||token[1].equalsIgnoreCase("DC")){
                Symtable[symline][0]=token[0];
                Symtable[symline][1]=Integer.toString(LC);
                Symtable[symline][2]=Integer.toString(1);
                symline++;
            }
            else if(token.length==3 && token[2].charAt(0)=='='){
                Littable[litline][0]=token[2];
                Littable[litline][1]=Integer.toString(LC);
                litline++;
            }
            else{
                Optable[opline][0]=token[1];
                if(token[1].equalsIgnoreCase("START")||token[1].equalsIgnoreCase("END")||token[1].equalsIgnoreCase("EQU")||token[1].equalsIgnoreCase("LTORG") ){
                    Optable[opline][1]="AD";
                    Optable[opline][2]="R11";
                }
                else if(token[1].equalsIgnoreCase("DS")||token[1].equalsIgnoreCase("DC")){
                    Optable[opline][1]="DL";
                    Optable[opline][2]="R7";
                }
                else{
                    Optable[opline][1]="IS";
                    Optable[opline][2]="(04,1)";
                }
                opline++;
            }
            line_count++;
            LC++;
        }

        System.out.println("_________");
        System.out.println("\n\n    SYMBOL TABLE         ");
        System.out.println("SYMBOL\tADDRESS\tLENGTH");
        for(int i=0;i<symline;i++){
            System.out.println(Symtable[i][0]+"\t"+Symtable[i][1]+"\t"+Symtable[i][2]);
            System.out.println("--------------------------");
        }
        System.out.println();
        System.out.println("______________");
        System.out.println("\n\n  LITERAL TABLE            ");
        System.out.println("LITERAL\tADDRESS");
        System.out.println("---------------------");
        for(int i=0;i<litline;i++){
            System.out.println(Littable[i][0]+"\t"+Littable[i][1]);
            System.out.println("-----------------------");
        }
        
        System.out.println("______________");
        System.out.println("\n\n  OPCODE TABLE            ");
        System.out.println("MNEMONICS\tCLASS\tINFO");
        System.out.println("---------------------");
        for(int i=0;i<opline;i++){
            System.out.println(Optable[i][0]+"\t"+Optable[i][1]+"\t"+Optable[i][2]);
            System.out.println("-----------------------");
        }
    
        bf.close();

    }
}