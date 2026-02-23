/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   flood_fill.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/23 16:32:17 by pmarcos-          #+#    #+#             */
/*   Updated: 2026/02/23 17:01:48 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

 typedef struct  s_point
 {
   int           x;
   int           y;
 }               t_point;

void fill(char **tab, t_point size, char target, int row, int col)
{
    if (row < 0 || col < 0 || row >= size.y || col >= size.x)
        return;
    
    if (tab[row][col] == 'F' || tab[row][col] != target)
        return;

    tab[row][col] = 'F';
    fill(tab, size, target, row -1, col);
    fill(tab, size, target, row +1, col);
    fill(tab, size, target, row, col - 1);
    fill(tab, size, target, row, col + 1);
}

void flood_fill(char **tab, t_point size, t_point begin)
{
    char target = tab[begin.y][begin.x];
    fill(tab, size, target, begin.y, begin.x);
}
