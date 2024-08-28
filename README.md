# mayllu

Integrantes: 

-> Gabriel Blanco

```cpp

jiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii
#include <cstring>
#include <iosfwd>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

struct Matricula {
public:
  string codigo;
  int ciclo;
  float mensualidad;
  string observaciones;
  
  Matricula () {};

  Matricula (string codigo, int ciclo, float mensualidad, string observaciones) {
    this->codigo = codigo;
    this->ciclo = ciclo;
    this->mensualidad = mensualidad;
    this->observaciones = observaciones;
  };

  void show() {
    cout 
      << codigo << " | "
      << ciclo << " | "
      << mensualidad << " | "
      << observaciones << " | "
      << endl;
  };
};

class VariableRecord {
private:
  string data_filename = "data.bat";
  string metadata_filename = "metadata.bat";

public:
  VariableRecord(string _data_filename, string _metadata_filename) : data_filename(_data_filename), metadata_filename(_metadata_filename) {};

  vector<Matricula> load() {
    vector<Matricula> records;
    ifstream datafile(this->data_filename, ios::binary);
    if (!datafile.is_open()) throw runtime_error("Error. No se pudo abrir el archivo");

    while (true) {
      // read the size of the code
      int codigo_size, observaciones_size, ciclo;
      float mensualidad;
      if (!datafile.read((char*) (&codigo_size), sizeof(int))) break;

      // read the buffer cuz we know the size, add \0 for char with null at the end 
      char* codigo_buffer = new char[codigo_size + 1];
      datafile.read(codigo_buffer, codigo_size);
      codigo_buffer[codigo_size] = '\0';

      if (!datafile.read((char*) (&ciclo), sizeof(int))) break;
      if (!datafile.read((char*) (&mensualidad), sizeof(float))) break;
      if (!datafile.read((char*) (&observaciones_size), sizeof(int))) break;

      // samee !! as the top :)
      char* observaciones_buffer = new char[observaciones_size + 1]; 
      datafile.read(observaciones_buffer, observaciones_size);
      observaciones_buffer[observaciones_size] = '\0';

      // update instead of unpack a buffer
      Matricula current_record(string(codigo_buffer), ciclo, mensualidad, string(observaciones_buffer));

      current_record.show();
      records.push_back(current_record);

      delete[] codigo_buffer;
      delete[] observaciones_buffer;
    }

    datafile.close();
    return records;
  }

  void print_metadata() {
    ifstream file_metadata(this->metadata_filename, ios::binary);
    if (!file_metadata.is_open()) throw runtime_error("Error. No se pudo abrir el archivo de metadatos");
    
    cout << " | " << "Posición" << " | " << "Tamaño" << endl;
    streampos head_pos;

    while (file_metadata.read((char*) (&head_pos), sizeof(streampos))) {
      cout << head_pos << endl;
    }

    file_metadata.close();
  }

  void add (Matricula record) {
    ofstream file_metadata(this->metadata_filename, ios::app | ios::binary);
    ofstream file_data(this->data_filename, ios::app | ios::binary);
    int codigo_size, observaciones_size;

    codigo_size = record.codigo.size();
    file_data.write((char*) &(codigo_size), sizeof(int));
    file_data.write(record.codigo.c_str(), codigo_size);

    file_data.write((char*) &(record.ciclo), sizeof(int));
    file_data.write((char*) &(record.mensualidad), sizeof(float));

    observaciones_size = record.observaciones.size();
    file_data.write((char*) &(observaciones_size), sizeof(int)); 
    file_data.write(record.observaciones.c_str(), observaciones_size);

    streampos current_position = file_data.tellp();
    streampos recovery_last_size;
    streampos record_size = int(current_position) + sizeof(int) + codigo_size + sizeof(int) + sizeof(float) + sizeof(int) + observaciones_size;
  
    file_metadata.write((char*) (&record_size), sizeof(streampos));

    file_metadata.close();
    file_data.close();
  };

  void read_record(int pos) {
    ifstream file_metadata(this->metadata_filename, ios::binary);
    ifstream file_data(this->data_filename, ios::binary);
    if (!file_data.is_open()) throw runtime_error("Error. No se pudo abrir el archivo");
    if (!file_metadata.is_open()) throw runtime_error("Error. No se pudo abrir el archivo");

    int pos_fisica, size_record;

    file_metadata.seekg(pos * sizeof(int) * 2);
    file_metadata.read(reinterpret_cast<char*>(&pos_fisica), sizeof(int));
    file_metadata.read(reinterpret_cast<char*>(&size_record), sizeof(int));
    file_metadata.close();

    file_data.seekg(pos_fisica);

    int codigo_size, observaciones_size, ciclo;
    float mensualidad;

    file_data.read(reinterpret_cast<char*>(&codigo_size), sizeof(int));

        char* codigo_buffer = new char[codigo_size + 1];
        file_data.read(codigo_buffer, codigo_size);
        codigo_buffer[codigo_size] = '\0';

        file_data.read(reinterpret_cast<char*>(&ciclo), sizeof(int));
        file_data.read(reinterpret_cast<char*>(&mensualidad), sizeof(float));

        file_data.read(reinterpret_cast<char*>(&observaciones_size), sizeof(int));

        char* observaciones_buffer = new char[observaciones_size + 1];
        file_data.read(observaciones_buffer, observaciones_size);
        observaciones_buffer[observaciones_size] = '\0';

        file_data.close();

        Matricula current_record(string(codigo_buffer), ciclo, mensualidad, string(observaciones_buffer));

        current_record.show();

        delete[] codigo_buffer;
        delete[] observaciones_buffer;
    }
};

int main() {
  VariableRecord record_manager("data_p3_data.dat", "data_p3_metadata.dat");
  
  vector<Matricula> record_loaded = record_manager.load();
  for (Matricula &each_record : record_loaded) each_record.show();
  
  Matricula matricula_new_record("CODE777", 7, 7, "Observation 7771");
  record_manager.add(matricula_new_record);

  vector<Matricula> record_loaded_new = record_manager.load();
  for (Matricula &each_record : record_loaded_new) each_record.show();
  
  cout << "> Leyendo en posicion 10 usando metadata" << endl;
  record_manager.read_record(0);

  cout << "> Manager print metadata" << endl;
  record_manager.print_metadata();

  cout << sizeof(streampos) << endl;
  return 0;
};
```

