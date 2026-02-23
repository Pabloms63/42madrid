/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_range.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/23 22:02:21 by pmarcos-          #+#    #+#             */
/*   Updated: 2026/02/23 23:15:54 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>

int *ft_range(int start, int end)
{
    int len;
    int step;
    int i = 0;
    int *arr;

    if (start <= end)
    {
        len = end - start + 1;
        step = 1;
    }
    else
    {
        len = start - end + 1;
        step = -1;
    }
    arr = malloc(sizeof(int) * len);
    if (!arr)
        return NULL;
    while (i < len)
    {
        arr[i] = start;
        start += step;
        i++;
    }
    return arr;
}
