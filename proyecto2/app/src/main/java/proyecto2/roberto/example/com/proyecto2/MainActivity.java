package proyecto2.roberto.example.com.proyecto2;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import org.apache.http.HttpResponse;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.util.EntityUtils;
import android.os.StrictMode;

import com.squareup.okhttp.FormEncodingBuilder;
import com.squareup.okhttp.OkHttpClient;
import com.squareup.okhttp.Request;
import com.squareup.okhttp.RequestBody;

import java.net.MalformedURLException;
import java.net.URL;


public class MainActivity extends AppCompatActivity implements View.OnClickListener {
    public static OkHttpClient webClient = new OkHttpClient();
    EditText texto1,texto2;
    Button boton;
    TextView  registrar;
    String cadena="mario";
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        StrictMode.ThreadPolicy p = new StrictMode.ThreadPolicy.Builder().permitAll().build();
        StrictMode.setThreadPolicy(p);

        texto1=(EditText)findViewById(R.id.editText);
        texto2=(EditText)findViewById(R.id.editText2);
        boton =(Button)findViewById(R.id.button);
        registrar=(TextView) findViewById(R.id.textViewR);
        //boton.setOnClickListener(this);

        registrar.setOnClickListener(this);
        boton.setOnClickListener(this);



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
        if(v.getId()==R.id.textViewR){

                    Intent i = new Intent(this, Main2Activity.class );
                    startActivity(i);



        }
        if(v.getId()==R.id.button){

            RequestBody formBody = new FormEncodingBuilder()

                    .add("","")

                    .build();

            String respuesta=getString(texto2.getText().toString()+"/"+texto1.getText().toString()+"/prueba/", formBody);

            if(respuesta.equalsIgnoreCase("true")){

                Intent i = new Intent(this, Main3Activity.class );
                i.putExtra("parametro","Bienvenido al Sistema Drive: "+texto2.getText().toString());
                i.putExtra("usuario",texto2.getText().toString());
                startActivity(i);




            }else{

                Toast.makeText(getBaseContext(),respuesta,Toast.LENGTH_SHORT).show();
            }


        }





    }

    /**
     * Created by Roberto on 04/05/2017.
     */


}

