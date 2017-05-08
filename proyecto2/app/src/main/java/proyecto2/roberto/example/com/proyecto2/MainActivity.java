package proyecto2.roberto.example.com.proyecto2;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    TextView texto;
    Button boton;
    EditText dt1,dt2;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        texto=(TextView)findViewById(R.id.textView);
        texto.setText("hola mundo");
        boton=(Button)findViewById(R.id.button);
        dt1=(EditText)findViewById(R.id.editText);
        dt2=(EditText)findViewById(R.id.editText2);
    }
}
