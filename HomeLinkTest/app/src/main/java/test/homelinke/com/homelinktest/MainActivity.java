package test.homelinke.com.homelinktest;

import android.net.Uri;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Base64;
import android.util.Log;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;


public class MainActivity extends AppCompatActivity {
    //        final String source = "https://app.api.lianjia.com/house/ershoufang/detailpart1?house_code=101102129995&agent_type=1&request_ts=1511768107";
//    final String source = "https://app.api.lianjia.com/house/ershoufang/searchv4?city_id=110000&priceRequest=&limit_offset=0&moreRequest=&communityRequset=&has_recommend=1&is_suggestion=0&limit_count=20&sugQueryStr=&comunityIdRequest=&areaRequest=&is_history=0&schoolRequest=&condition=&roomRequest=&isFromMap=false&request_ts=1511327905";
//    final String source="https://app.api.lianjia.com/house/chengjiao/detailpart1?house_code=101102035004&request_ts=1511334292";
//    final String source="https://app.api.lianjia.com/house/zufang/searchV2?city_id=110000&priceRequest=&limit_offset=0&moreRequest=&communityRequset=&is_suggestion=0&limit_count=20&sugQueryStr=&comunityIdRequest=&areaRequest=&is_history=0&condition=&roomRequest=&isFromMap=false&request_ts=1511339341";
//    final String source = "https://app.api.lianjia.com/house/ershoufang/detailpart1?house_code=101102233336&agent_type=1&request_ts=1511345004";
//    final String source = "https://app.api.lianjia.com/house/house/moreinfo?house_code=101102055046&request_ts=1511345701";
    final String source = "https://app.api.lianjia.com/house/ershoufang/searchv4?city_id=110000&priceRequest=&limit_offset=2100&moreRequest=&communityRequset=&has_recommend=1&is_suggestion=0&limit_count=20&sugQueryStr=&comunityIdRequest=&areaRequest=&is_history=0&schoolRequest=&condition=&roomRequest=&isFromMap=false&request_ts=1511776535";


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        String encripty = encripty(source, null);

    }

    public String encripty(String str, Map<String, String> map) {
        Map parmars = getParmars(str);
        HashMap hashMap = new HashMap();
        if (parmars != null) {
            hashMap.putAll(parmars);
        }
        if (map != null) {
            hashMap.putAll(map);
        }
        List arrayList = new ArrayList(hashMap.entrySet());
        Collections.sort(arrayList, new Comparator() {
            @Override
            public int compare(Object obj, Object obj2) {
                return a((Map.Entry) obj, (Map.Entry) obj2);
            }

            public int a(Map.Entry<String, String> entry, Map.Entry<String, String> entry2) {
                return ((String) entry.getKey()).compareTo((String) entry2.getKey());
            }
        });

        String GetAppSecret = "93273ef46a0b880faf4466c48f74878f";
        String GetAppId = "20170324_android";
        StringBuilder stringBuilder = new StringBuilder(GetAppSecret);
        for (int i = 0; i < arrayList.size(); i++) {
            Map.Entry entry = (Map.Entry) arrayList.get(i);
            stringBuilder.append(((String) entry.getKey()) + "=" + ((String) entry.getValue()));
        }
        Log.d("ssssStringBuilder:", stringBuilder.toString());
        Log.d("ssssSHA1:", Digest_SHA1(stringBuilder.toString()));
        Log.d("ssss", GetAppId + ":" + Digest_SHA1(stringBuilder.toString()));
        Log.d("sssstime", String.valueOf(System.currentTimeMillis() / 1000));
        GetAppSecret = Base64.encodeToString((GetAppId + ":" + Digest_SHA1(stringBuilder.toString())).getBytes(), 2);

        Log.d("sssss", GetAppSecret);
        return new String("helloworld");


    }

    public static String Digest_SHA1(String str) {
        try {
            MessageDigest instance = MessageDigest.getInstance("SHA-1");
            instance.update(str.getBytes());
            byte[] digest = instance.digest();
            StringBuffer stringBuffer = new StringBuffer();
            for (byte b : digest) {
                String toHexString = Integer.toHexString(b & 255);
                if (toHexString.length() < 2) {
                    stringBuffer.append(0);
                }
                stringBuffer.append(toHexString);
            }
            return stringBuffer.toString();
        } catch (NoSuchAlgorithmException e) {
            e.printStackTrace();
            return "";
        }
    }

    private Map<String, String> getParmars(String str) {
        if (str == null || str.length() == 0) {
            return null;
        }
        HashMap hashMap = new HashMap();
        Uri parse = Uri.parse(str);
        for (String str2 : parse.getQueryParameterNames()) {
            String str22 = str2.toString();
            hashMap.put(str22, parse.getQueryParameter(str22));
        }
        return hashMap;
    }
}
