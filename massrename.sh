# Requiere sudo apt install -y rename
# Renombra sanitizando lo tipico, dejando menos archivos por renombrar correctamente
rename -e ' # -n para no hacer el cambio permanente
  s/^[^-]+ - //;                 # 1. Quita todo antes de " - "
  s/\s*\([^)]*\)//g;            # 2. Quita todo entre paréntesis, con espacio opcional antes
  s/\s*\[[^]]*\]//g;            # 3. Quita todo entre corchetes, con espacio opcional antes
  s/\s*live\s*\@\s*[^()\[\]]+//ig; # 4. Quita "live @ algo"
  s/\s*(ft\.?|feat\.?|featuring)\s+[^()\[\]-]+//ig; # 5. Quita "ft. artista"
  s/["＂]//g;                        # 6. Quita comillas
  s/\b\d{4}\b//g;                   # 7. Quita años
  s/^[^-]+ - //;                    # 8. Reaplica si volvió artista
  s/[^\x20-\x7E]//g;                # 9. Quita caracteres no imprimibles
  s/\s{2,}/ /g;                     # 10. Reduce espacios dobles
  s/^\s+|\s+$//g;                   # 11. Trim espacios
  s/\.+/./g;                        # 12. Reduce puntos múltiples
  s/\.mp3$//i;                      # 13. Quita extensión temporalmente
  s/\.+$//;                         # 14. Quita punto final si quedó
  $_ .= ".mp3";                     # 15. Vuelve a poner extensión
' *.mp3
