"""Desktop Keyboard Lab: capture only the focused input in this own window."""
from model import Session


def main():
    import tkinter as tk
    from tkinter import filedialog, messagebox, ttk
    session = Session()
    window = tk.Tk()
    window.title('Keyboard Event Lab · registro visible')
    window.geometry('940x620')
    window.minsize(680, 440)
    frame = ttk.Frame(window, padding=24)
    frame.pack(fill='both', expand=True)
    ttk.Label(frame, text='Observa cómo responde tu teclado', font=('Segoe UI', 22)).pack(anchor='w')
    ttk.Label(frame, text='Solo se registran pulsaciones dentro del área de escritura de esta ventana.\nInicia para registrar; pausa cuando termines. No escribas información sensible.').pack(anchor='w', pady=12)
    status = tk.StringVar(value='Registro pausado · 0 eventos')
    ttk.Label(frame, textvariable=status).pack(anchor='w', pady=6)
    controls = ttk.Frame(frame)
    controls.pack(fill='x', pady=8)
    panes = ttk.Panedwindow(frame, orient='horizontal')
    panes.pack(fill='both', expand=True)
    entry = tk.Text(panes, wrap='word', font=('Segoe UI', 13), width=35, height=16)
    console = tk.Text(panes, wrap='none', font=('Consolas', 11), width=43, height=16, state='disabled')
    panes.add(entry, weight=1)
    panes.add(console, weight=1)

    def refresh():
        state = 'Activo en el área de escritura' if session.active else 'Registro pausado'
        status.set(f'{state} · {len(session.events)} eventos (máximo {session.limit})')

    def start():
        session.start()
        refresh()
        entry.focus_set()

    def pause():
        session.pause()
        refresh()

    def clear():
        session.clear()
        console.configure(state='normal')
        console.delete('1.0', 'end')
        console.configure(state='disabled')
        refresh()

    def export():
        if not session.events:
            messagebox.showinfo('Sin eventos', 'Inicia el registro y escribe en el área de prueba.')
            return
        target = filedialog.asksaveasfilename(defaultextension='.json', filetypes=[('JSON','*.json')], initialfile='keyboard-session.json')
        if target:
            try:
                with open(target, 'w', encoding='utf-8') as output:
                    output.write(session.export())
            except OSError:
                messagebox.showerror('No se pudo guardar', 'Elige una carpeta donde tengas permiso de escritura.')

    for label, action in [('Iniciar registro',start),('Pausar',pause),('Limpiar eventos',clear),('Exportar JSON',export)]:
        ttk.Button(controls, text=label, command=action).pack(side='left', padx=(0,8))

    def on_key(event):
        item = session.record(event.keysym, event.char)
        if item:
            console.configure(state='normal')
            console.insert('end', f'{item.sequence:04d}  {item.key:<16} {item.character!r}\n')
            lines = int(console.index('end-1c').split('.')[0])
            if lines > session.limit + 1:
                console.delete('1.0', '2.0')
            console.see('end')
            console.configure(state='disabled')
            refresh()
    entry.bind('<KeyPress>', on_key, add='+')
    # Neither bind_all nor pynput is used. Closing this window ends capture.
    window.mainloop()


if __name__ == '__main__':
    main()
