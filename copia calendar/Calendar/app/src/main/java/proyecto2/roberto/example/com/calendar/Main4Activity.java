package proyecto2.roberto.example.com.calendar;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.DatePicker;

public class Main4Activity extends AppCompatActivity {

    DatePicker calendario;
    Button evento;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main4);


        calendario=(DatePicker)findViewById(R.id.datePicker);
        evento=(Button)findViewById(R.id.button10);

        evento.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                Intent i = new Intent(getBaseContext(), Main3Activity.class );
                startActivity(i);

            }
        });
    }
}
