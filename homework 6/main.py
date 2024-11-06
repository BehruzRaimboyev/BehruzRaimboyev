import json
import os
from datetime import datetime

notes_file='notes.json'
def load_notes():
   
    if os.path.exists(notes_file):
        with open(notes_file,'rt') as file:
            return json.load(file)
        return []
def save_notes(notes):
    with open(notes_file,'w') as file:
        json.dump(notes,file,indent=4)
    
def show_all_notes(notes):
    if not notes:
        print('----------------there is no notes!\n please create a note to read---- :)')
        return
    for note in notes:
        print(f"ID:{note['id']}\ncreated:{note['created']}")

def show_note_details(notes,notes_id):
    note=next((note for note in notes if note['id']==notes_id),None)
    if note:
        print(f"ID:{note['id']}\n Text:{note['text']}\n created:{note['created']}")
    else:
        print('it not found!')

def create_note(notes,text):
    note_id=max([note['id'] for note in notes],default=0)+1
    created=datetime.now().strftime('%Year-%month-%day %H:%M:%Sec')
    new_note={
        'id':note_id,
        'text':text,
        'created':created
    }
    notes.append(new_note)
    save_notes(notes)
    print(f'note created with ID{note_id}.')
def update_note(notes,note_id,new_text):
    note=next((note for note in notes if note['id']==note_id),None)
    if note:
        note['text']=new_text
        save_notes(notes)
        print(f'noten_id:{note_id} updated :)')
    else:
        print("note didn't updated!")
def delete_note(notes,note_id):
    note=next((note for note in notes if note['id']==note_id),None)
    if note:
        notes.remove(note)
        save_notes(notes)
        print('note with {note_id} this id deleted!')
    else:
        print('note not found')


def main():
    notes=load_notes()

    while True:
        print("\n Notebook Application ")
        print("1. Show All Notes")
        print("2. Show Note Details")
        print("3. Create Note")
        print("4. Update Note")
        print("5. Delete Note")
        print("6. Exit")

        choice =input('Choose option:')

        if choice =='1':
            show_all_notes(notes)

        elif choice =='2':
            note_id=int('give an ID of note:')
            show_note_details(notes,note_id)
        
        elif choice =='3':
            text=input('give note text:')
            create_note(notes,text)

        elif choice=='4':
            note_id=input('give an id to update:')
            new_text=input('give new text:')
            update_note(notes,note_id,new_text)
        elif choice =='5':
            note_id=input('give an id to delete:')
            delete_note(notes,note_id)
        
        elif choice =='6':
            print('You exit the program,BYE!')
            break
        else:
            print('invalid choice try again!.')
if __name__=='__main__':
    main()
