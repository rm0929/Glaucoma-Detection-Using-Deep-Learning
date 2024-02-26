public class test{

    private static boolean inRange(String track){
        int value = Integer.valueOf(track);
        if(value == 32){
            return true;
        }
        else if(value >= 65 && value <= 90){
            return true;
        }else if(value >= 97 && value <= 122){
            return true;
        }else{
            return false;
        }
    }

    private static char getValue(String track){
        int value = Integer.valueOf(track);
        return (char)value;
    }

    private static String convert(String encode){
        String decode = "";
        String track = "";
        for(int i = encode.length() - 1; i >= 0; i--){
            track += encode.charAt(i);
            if(inRange(track)){
                decode += getValue(track);
                track = "";
            }
        }

        return decode;
    }

    public static void main(String[] args){
        System.out.println((int)'s');

        System.out.println(convert("23511011501782351112179911801562340161171141148"));
    }
}
// 32
// 65-90
// 97-122