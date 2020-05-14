��    $      <  5   \      0  �   1  �   �  a   �     �  R  �  N   E  &   �  O   �       #     !   =  *   _  &   �  &   �  (   �               (  (   6  '   _  4   �  4   �  &   �  /   	  /   H	  7   x	  -   �	  %   �	  %   
  "   *
     M
  .   c
  #   �
  '   �
     �
  �  �
  �   y  �   J  u   �     u  �  �  }   6  ;   �  R   �     C  )   S  4   }  <   �  '   �  '     2   ?  #   r     �     �  4   �  *   �  2     2   G  #   z  +   �  +   �  5   �  9   ,  (   f  2   �  .   �     �  9     )   G  ;   q     �                        
   !                                                                                               $              #      	          "                              -T, --tr46t              Enable TR46 transitional processing
  -N, --tr46nt             Enable TR46 non-transitional processing
      --no-tr46            Disable TR46 processing
   -d, --decode             Decode (punycode) domain name
  -l, --lookup             Lookup domain name (default)
  -r, --register           Register label
   -h, --help               Print help and exit
  -V, --version            Print version and exit
 Charset: %s
 Command line interface to the Libidn2 implementation of IDNA2008.

All strings are expected to be encoded in the locale charset.

To process a string that starts with `-', for example `-foo', use `--'
to signal the end of parameters, as in `idn2 --quiet -- -foo'.

Mandatory arguments to long options are mandatory for short options too.
 Internationalized Domain Name (IDNA2008) convert STRINGS, or standard input.

 Try `%s --help' for more information.
 Type each input string on a line by itself, terminated by a newline character.
 Unknown error Usage: %s [OPTION]... [STRINGS]...
 could not convert string to UTF-8 could not determine locale encoding format domain label longer than 63 characters domain name longer than 255 characters input A-label and U-label does not match input A-label is not valid input error out of memory punycode conversion resulted in overflow punycode encoded data will be too large string contains a context-j character with null rule string contains a context-o character with null rule string contains a disallowed character string contains a forbidden context-j character string contains a forbidden context-o character string contains a forbidden leading combining character string contains forbidden two hyphens pattern string contains invalid punycode data string contains unassigned code point string could not be NFC normalized string encoding error string has forbidden bi-directional properties string is not in Unicode NFC format string start/ends with forbidden hyphen success Project-Id-Version: libidn2 2.0.4
Report-Msgid-Bugs-To: bug-libidn2@gnu.org
PO-Revision-Date: 2017-12-17 09:30+0100
Last-Translator: Jakub Bogusz <qboosh@pld-linux.org>
Language-Team: Polish <translation-team-pl@lists.sourceforge.net>
Language: pl
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit
X-Bugs: Report translation errors to the Language-Team address.
   -T, --tr46t              Włączenie przetwarzania przejściowego TR46
  -N, --tr46nt             Włączenie przetwarzania nieprzejściowego TR46
      --no-tr46            Wyłączenie przetwarzania TR46
   -d, --decode             Zakodowanie (w punycode) nazwy domeny
  -l, --lookup             Wyszukanie nazwy domeny (domyślne)
  -r, --register           Zarejestrowanie etykiety
   -h, --help               Wypisanie opisu i zakończenie
  -V, --version            Wypisanie wersji i zakończenie
 Zestaw znaków: %s
 Jest to interfejs linii poleceń do implementacji Libidn2 standardu IDNA2008.

Wszystkie łańcuchy powinny być zakodowane w zestawie znaków właściwym dla
używanej lokalizacji.

Aby przetworzyć łańcuch zaczynający się od `-', np. `-foo', należy użyć
`--', aby zasygnalizować koniec parametrów, np. `idn2 --quiet -- -foo'.

Argumenty obowiązkowe dla długich opcji są również obowiązkowe dla opcji
krótkich.
 Program konwertuje ŁAŃCUCHY lub standardowe wyjście zgodnie ze standardem
IDNA2008 dla umiędzynarodowionych nazw domen.

 Polecenie `%s --help' pozwoli uzyskać więcej informacji.
 Należy podać każdy łańcuch w osobnej linii, zakończony znakiem nowej linii.
 Nieznany błąd Składnia: %s [OPCJA]... [ŁAŃCUCHY]...
 nie udało się przekonwertować łańcucha na UTF-8 nie udało się określić formatu kodowania dla lokalizacji etykieta domeny dłuższa niż 63 znaki nazwa domeny dłuższa niż 255 znaków wejściowe etykiety A oraz U nie pasują do siebie wejściowa etykieta A jest błędna błąd wejścia brak pamięci konwersja punycode zakończyła się przepełnieniem dane zakodowane punycode będą zbyt duże łańcuch zawiera znak context-j z pustą regułą łańcuch zawiera znak context-o z pustą regułą łańcuch zawiera niedozwolony znak łańcuch zawiera zabroniony znak context-j łańcuch zawiera zabroniony znak context-o łańcuch zawiera zabroniony wiodący znak łączący łańcuch zawiera zabroniony wzorzec z dwoma łącznikami łańcuch zawiera błędne dane punycode łańcuch zawiera nieprzypisaną wartość kodową normalizacja NFC łańcucha nie powiodła się błąd kodowania łańcucha łańcuch ma zabronione własności dwukierunkowego pisma łańcuch nie jest w formacie Unicode NFC łańcuch zaczyna się lub kończy zabronionym łącznikiem sukces 