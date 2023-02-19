from django.db import models

# Create your models here.
class Pelicula(models.Model):
    titulo = models.CharField(max_length=200)
    genero = models.CharField(max_length=200)
    dierector = models.CharField(max_length=200, blank=True)
    fecha = models.DateField
    descargada = models.BooleanField(default=False, blank=True)
    
    def __str__(self):
        return self.titulo

class Serie(models.Model):
    titulo = models.CharField(max_length=200)
    genero = models.CharField(max_length=200)
    fecha = models.DateField
    temporadas = models.IntegerField(default=1)
    completada = models.BooleanField(default=False)
    descargada = models.BooleanField(default=False, blank=True)
    
    def __str__(self):
        return self.titulo

class Capitulos(models.Model):
    nuemero = models.IntegerField(default=0)
    temporada = models.IntegerField(default=0)
    serie = models.ForeignKey(Serie, on_delete= models.CASCADE)
    fecha_emision = models.DateTimeField
    
    def __str__(self):
        return self.serie.titulo + ""+ self.temporada+"x"+ self.nuemero

class Documentales(models.Model):
    nuemero = models.IntegerField(default=0)
    temporada = models.IntegerField(default=0)
    serie = models.ForeignKey(Serie, on_delete= models.CASCADE)
    fecha_emision = models.DateTimeField
    
    def __str__(self):
        return self.serie.titulo
        """
        pelicula= Pelicula(titulo='Roky', director="Sylvester Stallone")
        pelicula.save()
        lista.peliculas = Peliculas.objetcs.all()
        print(lista.pelicula)
        
        pielucula = Peliacula.objetct.get(titulo='Roky')
        print(pelicula.titulo)
        
        pielucula = Peliacula.objetct.get(titulo='Roky')
        pelicula.delete()
        
        pielucula = Peliacula.objetct.get(titulo='Roky')
        pelicula.director ='otro'
        pelicula.save()
        """