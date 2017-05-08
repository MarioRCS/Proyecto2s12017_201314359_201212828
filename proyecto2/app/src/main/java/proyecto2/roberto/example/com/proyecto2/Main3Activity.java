package proyecto2.roberto.example.com.proyecto2;

import android.Manifest;
import android.content.Context;
import android.content.DialogInterface;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.database.Cursor;
import android.net.Uri;
import android.os.Environment;
import android.os.FileUriExposedException;
import android.provider.MediaStore;
import android.support.annotation.NonNull;
import android.support.v4.app.ActivityCompat;
import android.support.v4.content.ContextCompat;
import android.support.v7.app.AlertDialog;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.test.mock.MockDialogInterface;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.Menu;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ListView;
import android.widget.TextView;
import android.widget.Toast;

import com.squareup.okhttp.FormEncodingBuilder;
import com.squareup.okhttp.OkHttpClient;
import com.squareup.okhttp.Request;
import com.squareup.okhttp.RequestBody;

import org.apache.commons.codec.binary.Base64;
import org.apache.http.entity.FileEntity;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.lang.reflect.Array;
import java.net.MalformedURLException;
import java.net.URISyntaxException;
import java.net.URL;
import java.nio.charset.Charset;
import java.util.logging.Level;
import java.util.logging.Logger;

import static android.R.attr.data;

public class Main3Activity extends AppCompatActivity implements View.OnClickListener{
    public static OkHttpClient webClient = new OkHttpClient();
    ListView lis,lis2;
    String[] nombres={""};
    TextView usuario;
    EditText ruta;
    Button actualizar,nuevaCarpeta,cargararchivo,archivo,eliminarcarpeta,eliminararchivo;
    Button modificarcarpeta,modificararchivo;
    private static final int PICKER= 1;
    private static final int PICKER2= 1;
    EditText cajaarchivo;



    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main3);

        VerificarPermisos();
        usuario =(TextView)findViewById(R.id.textView);
        usuario.setText(getIntent().getExtras().getString("parametro"));

        actualizar =(Button)findViewById(R.id.button3);
        actualizar.setText("Actualizar Carpeta");
        ruta=(EditText)findViewById(R.id.editText3);
        ruta.setEnabled(true);
        ruta.setText(getIntent().getExtras().getString("usuario")+"A"+"root");
        actualizar.setOnClickListener(this);
        nuevaCarpeta=(Button)findViewById(R.id.button4);
        nuevaCarpeta.setText("Crear Nueva Carpeta");
        nuevaCarpeta.setOnClickListener(this);

        cargararchivo=(Button)findViewById(R.id.button6);
        cargararchivo.setOnClickListener(this);
        archivo=(Button)findViewById(R.id.button10);
        archivo.setOnClickListener(this);
        eliminarcarpeta=(Button)findViewById(R.id.button5);
        eliminarcarpeta.setOnClickListener(this);
        eliminararchivo=(Button)findViewById(R.id.button7);
        eliminararchivo.setOnClickListener(this);
        modificarcarpeta=(Button)findViewById(R.id.button8);
        modificarcarpeta.setOnClickListener(this);

        modificararchivo=(Button)findViewById(R.id.button9);
        modificararchivo.setOnClickListener(this);

    }



    @Override
    public void onClick(View v) {

        DescargarArchivo(v);
        if(v.getId()==R.id.button3){

            ActualizarCarpeta();

        }
        if(v.getId()==R.id.button4){

            CrearCarpeta();

                    }
        if(v.getId()==R.id.button6){

            CargarArchivo();
        }
        if(v.getId()==R.id.button10){

        ActualizarArchivo();

        }if (v.getId()==R.id.button5){

            EliminarCarpeta();

        }if (v.getId()==R.id.button7){

            EliminarArchivo();

        }if (v.getId()==R.id.button8){


            ModificarCarpeta();
        }if(v.getId()==R.id.button9){

            ModificarArchivo();

        }


    }



    public  void SubirArchivo(View view){

        String direccion[]=cajaarchivo.getText().toString().split("/");
        String nombreArchivo=direccion[direccion.length-1];
        String rutaArchivo=ruta.getText().toString();

        File fichero = new File(cajaarchivo.getText().toString());
        FileInputStream ficheroStream;

        try {
            ficheroStream = new FileInputStream(fichero);
            byte contenido[] = new byte[(int)fichero.length()];
            ficheroStream.read(contenido);
            ficheroStream.close();
            FileOutputStream ficheroStream2;
            String cadena = new String(Base64.encodeBase64(contenido));

            RequestBody formBody = new FormEncodingBuilder()

                    .add("","")

                    .build();

            String respuesta=getString(rutaArchivo+"/"+nombreArchivo+"/"+cadena+"/subirarchivo/",formBody);
            Toast.makeText(view.getContext(),respuesta,Toast.LENGTH_LONG).show();



        } catch (IOException ex) {
            System.out.println(ex.getMessage());
        }


    }


    public void EliminarArchivo(){

        View vista= LayoutInflater.from(Main3Activity.this).inflate(R.layout.eliminararchivo,null);
        final EditText caja2 = (EditText) vista.findViewById(R.id.editText7);
        //caja1.setText(nombre);
        AlertDialog.Builder build = new AlertDialog.Builder(Main3Activity.this);

        build.setMessage("Eliminar Archivo...")
                .setView(vista)
                .setPositiveButton("Eliminar", new DialogInterface.OnClickListener() {
                    @Override
                    public void onClick(DialogInterface dialog, int which) {

                        RequestBody formBody = new FormEncodingBuilder()

                                .add("","")

                                .build();
                        String respuesta=getString(ruta.getText().toString()+"/"+caja2.getText().toString()+"/eliminararchivo/", formBody);
                        Toast.makeText(getBaseContext(),respuesta,Toast.LENGTH_SHORT).show();

                    }
                }).setNegativeButton("Cancelar",null).setCancelable(false);

        AlertDialog dialogo = build.create();
        dialogo.show();

    }





    public void EliminarCarpeta(){

        View vista= LayoutInflater.from(Main3Activity.this).inflate(R.layout.eliminarcarpeta,null);
        final EditText caja2 = (EditText) vista.findViewById(R.id.editText6);
        //caja1.setText(nombre);
        AlertDialog.Builder build = new AlertDialog.Builder(Main3Activity.this);

        build.setMessage("Eliminar Carpeta...")
                .setView(vista)
                .setPositiveButton("Eliminar", new DialogInterface.OnClickListener() {
                    @Override
                    public void onClick(DialogInterface dialog, int which) {

                        RequestBody formBody = new FormEncodingBuilder()

                                .add("","")

                                .build();
                        String respuesta=getString(ruta.getText().toString()+"/"+caja2.getText().toString()+"/eliminarcarpeta/", formBody);
                        Toast.makeText(getBaseContext(),respuesta,Toast.LENGTH_SHORT).show();

                    }
                }).setNegativeButton("Cancelar",null).setCancelable(false);

        AlertDialog dialogo = build.create();
        dialogo.show();

    }


    public void ModificarCarpeta(){

        View vista= LayoutInflater.from(Main3Activity.this).inflate(R.layout.modificarcarpeta,null);
        final EditText caja2 = (EditText) vista.findViewById(R.id.editText8);
        final EditText caja3 = (EditText) vista.findViewById(R.id.editText9);
        //caja1.setText(nombre);
        AlertDialog.Builder build = new AlertDialog.Builder(Main3Activity.this);

        build.setMessage("Modificar Carpeta...")
                .setView(vista)
                .setPositiveButton("Modificar", new DialogInterface.OnClickListener() {
                    @Override
                    public void onClick(DialogInterface dialog, int which) {

                        RequestBody formBody = new FormEncodingBuilder()

                                .add("","")

                                .build();
                        String respuesta=getString(ruta.getText().toString()+"/"+caja2.getText().toString()+"/"+caja3.getText().toString()+"/modificarcarpeta/", formBody);
                        Toast.makeText(getBaseContext(),respuesta,Toast.LENGTH_SHORT).show();

                    }
                }).setNegativeButton("Cancelar",null).setCancelable(false);

        AlertDialog dialogo = build.create();
        dialogo.show();

    }


    public void ModificarArchivo(){

        View vista= LayoutInflater.from(Main3Activity.this).inflate(R.layout.modificararchivo,null);
        final EditText caja2 = (EditText) vista.findViewById(R.id.editText10);
        final EditText caja3 = (EditText) vista.findViewById(R.id.editText11);
        //caja1.setText(nombre);
        AlertDialog.Builder build = new AlertDialog.Builder(Main3Activity.this);

        build.setMessage("Modificar Archivo...")
                .setView(vista)
                .setPositiveButton("Modificar", new DialogInterface.OnClickListener() {
                    @Override
                    public void onClick(DialogInterface dialog, int which) {

                        RequestBody formBody = new FormEncodingBuilder()

                                .add("","")

                                .build();
                        String respuesta=getString(ruta.getText().toString()+"/"+caja2.getText().toString()+"/"+caja3.getText().toString()+"/modificararchivo/", formBody);
                        Toast.makeText(getBaseContext(),respuesta,Toast.LENGTH_SHORT).show();

                    }
                }).setNegativeButton("Cancelar",null).setCancelable(false);

        AlertDialog dialogo = build.create();
        dialogo.show();
    }








    public void CargarArchivo(){

        View vista= LayoutInflater.from(Main3Activity.this).inflate(R.layout.cargadocumentos,null);
         cajaarchivo = (EditText) vista.findViewById(R.id.editText4);
        Button cargar=(Button)vista.findViewById(R.id.button11);
        Button subir=(Button)vista.findViewById(R.id.button12);
        Button cancelar=(Button)vista.findViewById(R.id.button13);
        cargar.setText("Cargar Archivo");
        subir.setText("Subir Archivo");
        cancelar.setText("cancelar");

        cargar.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                pick();

            }
        });

        subir.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                SubirArchivo(v);

            }
        });

        AlertDialog.Builder build = new AlertDialog.Builder(Main3Activity.this);

        build.setMessage("Carga de Archivos")
                .setView(vista);

        AlertDialog dialogo = build.create();
        dialogo.show();

    }








    public void ActualizarArchivo(){

        for(int i=0;i<nombres.length;i++){

            nombres[i]="";
        }

        RequestBody formBody = new FormEncodingBuilder()
                .add("","")
                .build();
        String respuesta=getString(ruta.getText().toString()+"/actualizararchivos/", formBody);
        Toast.makeText(getBaseContext(),respuesta,Toast.LENGTH_SHORT).show();

        nombres=respuesta.split(",");

        lis=(ListView)findViewById(R.id.listview);
        final ArrayAdapter<String> adaptador=new ArrayAdapter<String>(this,android.R.layout.simple_expandable_list_item_1,nombres);
        lis.setAdapter(adaptador);

    }






            public void DescargarArchivo(View v){

                lis2=(ListView)findViewById(R.id.listview);
                final ArrayAdapter<String> adaptador=new ArrayAdapter<String>(this,android.R.layout.simple_expandable_list_item_1,nombres);
                lis2.setAdapter(adaptador);

                lis2.setOnItemClickListener(new AdapterView.OnItemClickListener() {
                    @Override
                    public void onItemClick(AdapterView<?> parent, View view, int position, long id) {

                        String nombre=(String) lis.getItemAtPosition(position);

                        View vista= LayoutInflater.from(Main3Activity.this).inflate(R.layout.descargararchivo,null);
                        final EditText caja1 = (EditText) vista.findViewById(R.id.editText5);
                        caja1.setText(nombre);
                        AlertDialog.Builder build = new AlertDialog.Builder(Main3Activity.this);

                        build.setMessage("¿Desea Descargar el Archivo?")
                                .setView(vista)
                                .setPositiveButton("Descargar", new DialogInterface.OnClickListener() {
                                    @Override
                                    public void onClick(DialogInterface dialog, int which) {

                                        RequestBody formBody = new FormEncodingBuilder()

                                                .add("","")

                                                .build();
                                        String respuesta=getString(ruta.getText().toString()+"/"+caja1.getText().toString()+"/descargararchivo/", formBody);
                                        Toast.makeText(getBaseContext(),"Archivo Descargado Correctamente",Toast.LENGTH_SHORT).show();

                                        String descarga[]=respuesta.split(",");
                                        FileOutputStream ficheroStream2;
                                        try {
                                            String nuevo= new String(descarga[0]);
                                            //byte[] contenido2=nuevo.getBytes(Charset.forName("UTF-8"));

                                            ficheroStream2= new FileOutputStream("/sdcard/"+descarga[1]);

                                            ficheroStream2.write(Base64.decodeBase64(nuevo.getBytes()));
                                            ficheroStream2.close();


                                        } catch (IOException ex) {
                                            System.out.println(ex.getMessage());
                                        }





                                    }
                                }).setNegativeButton("Cancelar",null).setCancelable(false);

                        AlertDialog dialogo = build.create();
                        dialogo.show();




                    }

                });



            }









    public void ActualizarCarpeta(){

        for(int i=0;i<nombres.length;i++){

            nombres[i]="";
        }

        RequestBody formBody = new FormEncodingBuilder()
                .add("","")
                .build();
        String respuesta=getString(ruta.getText().toString()+"/actualizarcarpeta/", formBody);
        Toast.makeText(getBaseContext(),respuesta,Toast.LENGTH_SHORT).show();

        nombres=respuesta.split(",");

        lis=(ListView)findViewById(R.id.listview);
        final ArrayAdapter<String> adaptador=new ArrayAdapter<String>(this,android.R.layout.simple_expandable_list_item_1,nombres);
        lis.setAdapter(adaptador);

        lis.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> parent, View view, int position, long id) {

                String nombre=(String) lis.getItemAtPosition(position);
                ruta.setText(ruta.getText().toString()+"A"+nombre);
                for(int i=0;i<nombres.length;i++){

                    nombres[i]="";
                }
                lis.setAdapter(null);
            }

        });

    }





    public void CrearCarpeta(){

        View vista= LayoutInflater.from(Main3Activity.this).inflate(R.layout.activity_crearcarpeta,null);
        final EditText caja = (EditText) vista.findViewById(R.id.txtCarpeta);
        AlertDialog.Builder build = new AlertDialog.Builder(Main3Activity.this);

        build.setMessage("Creación de Carpetas")
                .setView(vista)
                .setPositiveButton("Crear", new DialogInterface.OnClickListener() {
                    @Override
                    public void onClick(DialogInterface dialog, int which) {

                        //Toast.makeText(getBaseContext(),"diste en aceptar",Toast.LENGTH_SHORT).show();

                        RequestBody formBody = new FormEncodingBuilder()

                                .add("","")

                                .build();
                        String respuesta=getString(ruta.getText().toString()+"/"+caja.getText().toString()+"/crearcarpeta/", formBody);
                        Toast.makeText(getBaseContext(),respuesta,Toast.LENGTH_SHORT).show();
                    }
                }).setNegativeButton("Cancelar",null).setCancelable(false);

        AlertDialog dialogo = build.create();
        dialogo.show();

    }




    public void pick(){

        Intent intent= new Intent(Intent.ACTION_GET_CONTENT);
        intent.setType("*/*");
        intent.addCategory(Intent.CATEGORY_OPENABLE);
        try{

            startActivityForResult(Intent.createChooser(intent,"Selecciones el archivo"),PICKER);
        }catch(android.content.ActivityNotFoundException ex){

            Toast.makeText(this, "instale un explorador", Toast.LENGTH_SHORT).show();

        }


    }

    protected  void onActivityResult(int requestCode,int resultCode,Intent data){

        switch (requestCode){
            case PICKER:
                if (resultCode==RESULT_OK){

                    String path=data.getData().getPath();

                    cajaarchivo.setText(path);

                }
                break;

        }


    }




        private void VerificarPermisos(){
            if(ContextCompat.checkSelfPermission(Main3Activity.this,
                    Manifest.permission.WRITE_EXTERNAL_STORAGE)
                    != PackageManager.PERMISSION_GRANTED){

                if(ActivityCompat.shouldShowRequestPermissionRationale

                        (Main3Activity.this,Manifest.permission.WRITE_EXTERNAL_STORAGE)){

                }else{
                    ActivityCompat.requestPermissions(Main3Activity.this, new String[]{Manifest.permission.WRITE_EXTERNAL_STORAGE},PICKER2);
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


    @Override
    public void onRequestPermissionsResult(int requestCode, @NonNull String[] permissions, @NonNull int[] grantResults) {

        switch (requestCode){

            case PICKER2:
                if(grantResults.length>0 && grantResults[0]==PackageManager.PERMISSION_GRANTED){

                    //todo bien

                }else{



                }

            return;
        }


    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.

        return true;
    }



}
