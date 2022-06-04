from django.db import models
from django.utils.text import slugify


class Estudante(models.Model):
    nome = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Slug', max_length=130, editable=False)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Estudante'
        verbose_name_plural = 'Estudantes'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nome)
        super().save(*args, **kwargs)


class Cursos(models.Model):
    titulo = models.CharField('Título', max_length=100)
    slug = models.SlugField('Slug', max_length=130, editable=False)
    estudantes = models.ManyToManyField(Estudante, related_name='cursos', through='Avaliacoes')

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)


class Avaliacoes(models.Model):
    estudante = models.ForeignKey(Estudante, related_name='avaliacoes', on_delete=models.CASCADE)
    curso = models.ForeignKey(Cursos, related_name='avaliacoes', on_delete=models.CASCADE)
    avaliacao = models.PositiveSmallIntegerField()

    def __int__(self):
        return self.avaliacao

    def __repr__(self):
        return f'<Curso: {self.curso} - Avaliação: {self.avaliacao}>'

    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'
