#include <iostream>
#include <string>
#include <vector>
#include <tk.h>

using namespace std;

class StickyNotes {
public:
  StickyNotes() {
    root = tk_create_window(NULL, 800, 600, "Sticky Notes");
    listbox = tk_create_listbox(root, 0, 0, 600, 100);
    scrollbar = tk_create_scrollbar(root, tk_VERTICAL, 600, 0, 0, 100);
    tk_pack(listbox, side="left");
    tk_pack(scrollbar, side="right");
  }

  void AddNote(string note) {
    tk_insert(listbox, tk_END, note.c_str());
  }

  void CopySelectedNotes() {
    vector<string> selected_notes;
    int i = 0;
    while (i < tk_size(listbox)) {
      if (tk_get_selection(listbox, i)) {
        selected_notes.push_back(tk_get(listbox, i));
      }
      i++;
    }
    string notes = "";
    for (string note : selected_notes) {
      notes += note + "\n";
    }
    cout << notes;
  }

private:
  WINDOW *root;
  TCL_VAR *listbox;
  TCL_VAR *scrollbar;
};

int main() {
  StickyNotes sticky_notes;
  sticky_notes.AddNote("This is a sticky note.");
  sticky_notes.AddNote("This is another sticky note.");
  sticky_notes.CopySelectedNotes();
  tk_mainloop();
  return 0;
}
