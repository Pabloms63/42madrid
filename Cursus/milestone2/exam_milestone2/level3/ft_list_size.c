typedef struct    s_list
{
    struct s_list *next;
    void          *data;
}                 t_list;

int	ft_list_size(t_list *begin_list)
{
	int len = 0;
	while (begin_list)
	{
		begin_list = begin_list->next;
		len++;
	}
	return (len);
}
