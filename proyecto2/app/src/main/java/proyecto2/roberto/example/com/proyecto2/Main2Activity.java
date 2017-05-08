package proyecto2.roberto.example.com.proyecto2;

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

public class Main2Activity extends AppCompatActivity implements View.OnClickListener {
    public static OkHttpClient webClient = new OkHttpClient();

    EditText texto1,texto2;
    Button btnRegistrar;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main2);

        texto1=(EditText)findViewById(R.id.txtusuario);
        texto2=(EditText)findViewById(R.id.txtcontrasenia);
        btnRegistrar=(Button)findViewById(R.id.button2);

        btnRegistrar.setOnClickListener(this);
    }

    @Override
    public void onClick(View v) {

        if(v.getId()==R.id.button2){

            try{
                RequestBody formBody = new FormEncodingBuilder()

                        .add("","")

                        .build();

                String respuesta=getString(texto1.getText().toString()+"/"+texto2.getText().toString()+"/usuario/", formBody);

                Toast.makeText(getBaseContext(),respuesta,Toast.LENGTH_SHORT).show();
                texto1.setText("");
                texto2.setText("");

            }catch (Exception e){

                Toast.makeText(getBaseContext(),e.getMessage(),Toast.LENGTH_SHORT).show();

            }


        }
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

}
