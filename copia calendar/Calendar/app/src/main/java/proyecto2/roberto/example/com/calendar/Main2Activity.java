package proyecto2.roberto.example.com.calendar;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import com.squareup.okhttp.FormEncodingBuilder;
import com.squareup.okhttp.OkHttpClient;
import com.squareup.okhttp.Request;
import com.squareup.okhttp.RequestBody;

import java.net.MalformedURLException;
import java.net.URL;

public class Main2Activity extends AppCompatActivity implements View.OnClickListener{

    public static OkHttpClient webClient = new OkHttpClient();

    EditText usuario,contrasenia;
    Button registrar;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main2);

        usuario=(EditText)findViewById(R.id.Editext5);
        contrasenia=(EditText)findViewById(R.id.Editext4);
        registrar=(Button) findViewById(R.id.button2);
        registrar.setOnClickListener(this);


    }

    public void Registrar(){

        String respuesta="";
        RequestBody formBody = new FormEncodingBuilder()

                .add("","")
                .build();

        respuesta =getString(usuario.getText().toString()+"/"+contrasenia.getText().toString()+"/rcalendar/", formBody);

            Toast.makeText(getBaseContext(),respuesta,Toast.LENGTH_SHORT).show();


    }

    public String getString(String metodo, RequestBody formBody) {

        try {
            URL url = new URL("http://192.168.1.9:5000/" + metodo);
            Request req = new Request.Builder().url(url).get().build();
            com.squareup.okhttp.Response resp = webClient.newCall(req).execute();//Aqui obtiene la respuesta en dado caso si hayas pues un return en python
            String response_string = resp.body().string();//y este seria el string de las respuesta
            return response_string;
        } catch (MalformedURLException ex) {
            //java.util.logging.Logger.getLogger(proyecto2.TestWebServer.class.getName()).log(Level.SEVERE, null, ex);
            System.out.println(ex.getMessage());
        } catch (Exception ex) {
            //java.util.logging.Logger.getLogger(proyecto2.TestWebServer.class.getName()).log(Level.SEVERE, null, ex);
            System.out.println(ex.getMessage());
        }
        return null;
    }




    @Override
    public void onClick(View v) {

        if(v.getId()==R.id.button2){

            Registrar();

        }


    }
}
