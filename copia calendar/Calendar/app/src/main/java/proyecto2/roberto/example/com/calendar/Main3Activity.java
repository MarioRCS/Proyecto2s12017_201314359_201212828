package proyecto2.roberto.example.com.calendar;

import android.Manifest;
import android.annotation.SuppressLint;
import android.app.DatePickerDialog;
import android.content.DialogInterface;
import android.content.pm.PackageManager;
import android.icu.util.Calendar;
import android.os.Build;
import android.support.annotation.RequiresApi;
import android.support.v4.app.ActivityCompat;
import android.support.v7.app.AlertDialog;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.widget.Button;
import android.widget.CalendarView;
import android.widget.DatePicker;
import android.widget.EditText;
import android.widget.Toast;

import com.squareup.okhttp.FormEncodingBuilder;
import com.squareup.okhttp.RequestBody;

public class Main3Activity extends AppCompatActivity implements View.OnClickListener{

    EditText nombre,direccion,descripcion,hora,dia,mes,anio;
    Button crear,eliminar,modificar,btnhora,btndia,btnmes,btnanio;
    private int hhora,ddia,mmes,aanio;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main3);



        nombre=(EditText)findViewById(R.id.editText2);
        direccion=(EditText)findViewById(R.id.editText3);
        descripcion=(EditText)findViewById(R.id.editText5);
        hora=(EditText)findViewById(R.id.editText7);
        dia=(EditText)findViewById(R.id.editText9);
        mes=(EditText)findViewById(R.id.editText10);
        anio=(EditText)findViewById(R.id.editText11);


        crear=(Button)findViewById(R.id.button3);
        modificar=(Button)findViewById(R.id.button4);
        eliminar=(Button)findViewById(R.id.button5);

        crear.setOnClickListener(this);
        modificar.setOnClickListener(this);
        eliminar.setOnClickListener(this);

        btnhora=(Button)findViewById(R.id.button6);
        btndia=(Button)findViewById(R.id.button7);
        btnmes=(Button)findViewById(R.id.button8);
        btnanio=(Button)findViewById(R.id.button9);

        btnhora.setOnClickListener(this);
        btndia.setOnClickListener(this);
        btnmes.setOnClickListener(this);
        btnanio.setOnClickListener(this);


        dia.setText(getIntent().getExtras().getString("dia"));
        mes.setText(getIntent().getExtras().getString("mes"));
        anio.setText(getIntent().getExtras().getString("anio"));








    }


    public void arreglar(){

        View vista= LayoutInflater.from(Main3Activity.this).inflate(R.layout.calendario,null);
        final CalendarView caja2 = (CalendarView) vista.findViewById(R.id.calendarView);
        //caja1.setText(nombre);
        AlertDialog.Builder build = new AlertDialog.Builder(Main3Activity.this);

        build.setMessage("Eliminar Archivo...")
                .setView(vista);

        AlertDialog dialogo = build.create();
        dialogo.show();



    }


    @Override
    public void onClick(View v) {

        if(v.getId()==R.id.button6){

            arreglar();

        }

    }


}
