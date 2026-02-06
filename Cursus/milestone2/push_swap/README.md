This project has been created as part
of the 42 curriculum by pmarcos-

# PUSH_SWAP

## Índice
1. Descripción del proyecto
2. Instrucciones
3. Estrategia

---

## Descripción del proyecto

Push_swap es un proyecto de 42madrid que consiste en desarrollar un programa que ordene una serie de números enteros no dupicados utilizando dos pilas y un conjunto limitado de operaciones.

El programa recibe numeros enteros por argumentos y genera una secuencia de instrucciones para ordenar estos números en la pila A.
Estas son todas las operaciones que podemos usar:

- sa (swap a): Cambia los primeros dos elementos del principio de la pila A.
- sb (swap b): Exactamente igual que sa pero en la pila B.
- ss: sa y sb al mismo tiempo.
- pa (push a): Toma el primer elemento del principio de la pila B y lo coloca en el principio de la pila A.
- pb (push_b): Toma el primer elemento de principio de la pila A y lo coloca en el principio de la pila B.
- ra (rotate a): El primer elemento pasa a ser el último.
- rb (rotate b): Exactamente lo mismo pero en la pila B.
- rr: ra y rb al mismo tiempo.
- rra (reverse rotate a): El último elemento pasa a ser el primero.
- rrb (reverse rotate b): Exactamente lo mismo pero en la pila B.
- rrr: rra y rrb al mismo tiempo. 

---

## Instrucciones

Pasos a seguir para instalar, compilar y ejecutar el programa.

### Requisitos
- Compilador de C.
- Sistema operativo Linux/macOS.
- Make (Makefile).

### Instalación
- Clona este repositorio -> git clone <URL_DEL_REPOSITORIO>
- cd push_swap
- Compila el programa -> make.
- Ejecuta el programa pasando una lista de argumentos:
	ejemplo: ./push_swap 3 2 5 1 4

---

## Estrategia

He usado diferentes funciones para los casos en que recibimos 2, 3 y 4/5 argumentos. Y el algoritmo de ordenación radix + indexing cuando recibimos +5 números. En todas ellas aplica las operaciones señaladas en la descripción del proyecto.

void	sort_two(t_list **a)
{
	int	first;
	int	second;

	first = *(int *)(*a)-> content;
	second = *(int *)(*a)-> next -> content;
	if (first > second)
		sa(a);
}

void	sort_three(t_list **a)
{
	int	first;
	int	second;
	int	third;

	first = *(int *)(*a)-> content;
	second = *(int *)(*a)-> next -> content;
	third = *(int *)(*a)-> next -> next -> content;
	if (first > second && first < third)
		sa(a);
	else if (first > second && first > third && second < third)
		ra(a);
	else if (first > third && first < second)
		rra(a);
	else if (first < second && first < third && second > third)
	{
		sa(a);
		ra(a);
	}
	else if (first > second && first > third && second > third)
	{
		sa(a);
		rra(a);
	}
}

void	push_smallest_to_b(t_list **a, t_list **b)
{
	t_list	*tmp;
	int		min;
	int		pos;

	tmp = *a;
	min = *(int *)tmp->content;
	pos = 0;
	while (tmp)
	{
		if (*(int *)tmp->content < min)
		{
			min = *(int *)tmp->content;
			pos = 0;
		}
		tmp = tmp->next;
		pos++;
	}
	while (*(int *)(*a)->content != min)
	{
		if (pos <= ft_lstsize(*a) / 2)
			ra(a);
		else
			rra(a);
	}
	pb(a, b);
}

void	sort_five(t_list **a)
{
	t_list	*b;
	int		size;

	b = NULL;
	size = ft_lstsize(*a);
	if (size == 4)
	{
		push_smallest_to_b(a, &b);
		sort_three(a);
		pa(a, &b);
	}
	else if (size == 5)
	{
		push_smallest_to_b(a, &b);
		push_smallest_to_b(a, &b);
		sort_three(a);
		if (*(int *)(b->content) < *(int *)(b->next->content))
			sb(&b);
		pa(a, &b);
		pa(a, &b);
	}
}

void	radix_sort(t_list **a, int *nums, size_t size)
{
	t_list	*b;
	size_t	i;
	size_t	j;

	if (!a || !*a || size < 2)
		return ;
	b = NULL;
	sort_array(nums, size);
	i = 0;
	while (i < (size_t)max_bits(size))
	{
		j = 0;
		while (j < size)
		{
			if ((get_index(nums, size, *(int *)(*a)->content) >> i) & 1)
				ra(a);
			else
				pb(a, &b);
			j++;
		}
		while (b)
			pa(a, &b);
		i++;
	}
}
