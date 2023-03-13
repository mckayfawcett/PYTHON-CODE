public class Test{



    static String[][] Face = {
        {
            "0","1","2"
        },
        {
            "3","4","5"
        },
        {
            "6","7","8"
        }
    };


    
    static void show(String[][] Face){
        for(int i=0; i<3; i++){
            for(int j=0; j<3; j++){
                System.out.print(Face[i][j]);
            }
            System.out.println();
        }
    }

    static void rotateFace(String[][] Face, boolean clockwise){
        String[][] tempFace = new String[3][3];
        Face = tempFace;
        for(int i=0; i<3; i++){
            for(int j=0; j<3; j++){
                tempFace[i][j] = Face[i][j];
            }
        }


        if(clockwise){
            Face[0][0] = tempFace[0][2];
            Face[0][0] = tempFace[0][2];
            Face[0][0] = tempFace[0][2];
            Face[0][0] = tempFace[0][2];
            Face[0][0] = tempFace[0][2];
            Face[0][0] = tempFace[0][2];
            Face[0][0] = tempFace[0][2];
            Face[0][0] = tempFace[0][2];
            Face[0][0] = tempFace[0][2];
        }
        else{

        }

    }


    public static void main(String[] args){

        show(Face);

    }

}
