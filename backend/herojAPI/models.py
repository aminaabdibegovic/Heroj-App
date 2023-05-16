from django.db import models


class Korisnik(models.Model):
    ime = models.CharField(max_length=50)
    prezime = models.CharField(max_length=50)
    mail = models.CharField(max_length=50)

    def __str__(self):
        return self.mail


class PredavanjeVideo(models.Model):
    naslov = models.CharField(max_length=100)
    opis = models.TextField()
    link_videa = models.URLField()

    def __str__(self):
        return self.naslov


class PredavanjeDokumentacija(models.Model):
    id = models.AutoField(primary_key=True)
    naziv = models.CharField(max_length=255)
    opis = models.TextField()
    # treba skontati kako dokumentaciju, nije jednostavno... Softa
    dokumentacija = models.TextField()

    def __str__(self):
        return self.naziv


class Pitanja(models.Model):
    id = models.AutoField(primary_key=True)
    postavka = models.TextField()
    tacan_odgovor = models.TextField()
    tezina = models.IntegerField()

    def __str__(self):
        return self.postavka


class Nesrece(models.Model):
    korisnikid = models.ForeignKey(Korisnik, on_delete=models.CASCADE)
    vrsta = models.CharField(max_length=30)
    opis = models.TextField()

    def __str__(self):
        return self.vrsta


class PostupciPrvePomoci(models.Model):
    nesreca = models.ForeignKey(Nesrece, on_delete=models.CASCADE)
    opis = models.TextField()

    def __str__(self):
        return self.nesreca


class RezultatiTestiranja(models.Model):
    korisnikid = models.ForeignKey(Korisnik, on_delete=models.CASCADE)
    rezultat = models.BooleanField()

    def __str__(self):
        return self.rezultat


class HistorijaNesreca(models.Model):
    korisnikid = models.ForeignKey(Korisnik, on_delete=models.CASCADE)
    nesreca = models.ForeignKey(Nesrece, on_delete=models.CASCADE)

    def __str__(self):
        return self.korisnikid
