# Preparing the README.md content as described


# Kvadrat Tənlik Həll Edici

## Təsvir

Bu layihə Flask ilə yazılmış bir veb tətbiqdir və istifadəçilərə kvadrat tənliklərin həllini hesablamağa imkan verir. Proqram istifadəçinin daxil etdiyi `a`, `b`, `c` dəyərlərinə əsaslanaraq kvadrat tənliyin köklərini tapır və nəticəni ekranda göstərir.

## Xüsusiyyətlər

- **Flask Framework:** Python ilə yazılmış və veb tətbiqi üçün Flask istifadə olunur.
- **Real və Kompleks Kök Hesabı:** Diskriminanta (`D`) əsaslanaraq tənliyin iki real kökü, iki eyni kökü və ya iki kompleks kökü hesablanır.
- **Dinamik İstifadəçi İnterfeysi:** HTML formu ilə istifadəçinin daxil etdiyi məlumatlar qəbul edilir və nəticələr göstərilir.

## Fayllar

- **app.py**: Flask serveri və əsas hesablama məntiqini ehtiva edir.
- **index.js**: Tətbiqin JavaScript ilə istifadəçi qarşılıqlı əlaqələrini idarə edən kodu.
- **style.css**: Ümumi dizayn və görünüşü tənzimləyən CSS faylı.
- **index.html**: İstifadəçi interfeysini təmin edən əsas HTML faylı.

## Başlama

### Tələblər

- Python 3.x
- Flask

## İstifadə

1. `a`, `b`, `c` dəyərlərini formaya daxil edin.
2. `Hesabla` düyməsinə basaraq kvadrat tənliyin köklərini görün.
3. `Sıfırla` düyməsinə basaraq nəticəni təmizləyin.

## Əsas Məntiq

Proqram, istifadəçinin daxil etdiyi `a`, `b`, `c` dəyərlərinə əsaslanaraq kvadrat tənliyin diskriminantını (`D`) hesablayır:

- Əgər `D > 0` olarsa, iki fərqli real kök hesablanır.
- Əgər `D == 0` olarsa, iki eyni real kök hesablanır.
- Əgər `D < 0` olarsa, iki kompleks kök hesablanır.

## Töhfələr

Bu layihəyə töhfə verməkdən çəkinməyin! Fork edib pull request göndərə bilərsiniz.

## İstifadə Olunan Kitabxanalar

- **Flask**: Veb tətbiqləri yaratmaq üçün istifadə olunan mikro framework.
- **math**: Kvadrat tənliyin köklərini hesablamaq üçün riyazi funksiyaları təmin edir.
- **logging**: Tətbiqin loglama (jurnallaşdırma) məqsədi ilə istifadə olunur.

## Serveri işə salın:

````bash
python app.py

Brauzerinizdə bu ünvana gedərək tətbiqi işlədin:

http://127.0.0.1:5000


````
