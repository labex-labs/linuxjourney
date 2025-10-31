---
index: 4
lang: "es"
title: "Patrones de Búsqueda de Vim"
meta_title: "Patrones de Búsqueda de Vim - Texto Avanzado"
meta_description: "Aprenda a realizar búsquedas hacia adelante y hacia atrás en Vim usando patrones. Domine las técnicas de búsqueda de Vim para encontrar texto rápidamente y navegue por los resultados con 'n' y 'N'."
meta_keywords: "Búsqueda Vim, búsqueda Vim, comandos Vim, editor de texto Linux, tutorial Vim, guía Vim, patrones de búsqueda"
---

## Lesson Content

Buscar texto es una tarea fundamental en cualquier editor. Vim proporciona formas potentes y rápidas de realizar una `búsqueda en vim` directamente desde el modo normal. Exploremos cómo usar estos patrones de búsqueda para mejorar su flujo de trabajo.

### Búsqueda hacia adelante

Para realizar una `búsqueda en vim` hacia adelante estándar, simplemente presione la tecla `/` en modo normal, seguida de su término de búsqueda. Al presionar Enter, Vim saltará a la primera ocurrencia del término después de su cursor.

```plaintext
Mi archivo bonito es muy bonito.

/bonito

Esto encontrará la primera palabra "bonito" después del cursor.
```

### Búsqueda hacia atrás

De manera similar, puede buscar hacia atrás desde la posición de su cursor. Use la tecla `?` seguida de su término de búsqueda. Vim encontrará la primera ocurrencia antes de su cursor.

```plaintext
Mi archivo bonito es muy bonito.

?bonito

Esto encontrará primero la última palabra "bonito" en el archivo.
```

### Navegación de resultados de búsqueda

Una vez que se inicia una búsqueda, puede navegar fácilmente a través de todas las coincidencias en el archivo.

- Presione `n` para saltar a la **siguiente** coincidencia en la dirección de la búsqueda original.
- Presione `N` para saltar a la coincidencia **anterior**, moviéndose en la dirección opuesta a la búsqueda original.

### Búsqueda efectiva en Vim (Vim Lookup)

Los comandos `/` y `?` son el núcleo de cualquier operación de `búsqueda en vim` (vim lookup). Ya sea que necesite encontrar el nombre de una función específica, una variable o simplemente una palabra, este mecanismo de búsqueda es su herramienta principal. Dominar este simple proceso de `búsqueda en vim` (vim lookup) es esencial para una navegación y edición eficientes.

## Exercise

Para aplicar estos conceptos, pruebe el siguiente laboratorio práctico. Le ayudará a dominar las herramientas esenciales de edición de texto, incluidas las funcionalidades de búsqueda.

1. **[Editar archivos de texto en Linux con Vim y Nano](https://labex.io/es/labs/comptia-edit-text-files-in-linux-with-vim-and-nano-591076)** - Practique la creación, edición, guardado y navegación de archivos de texto con Vim y Nano.

## Quiz Question

¿Qué tecla se utiliza para iniciar una búsqueda hacia adelante en Vim?

## Quiz Answer

/
