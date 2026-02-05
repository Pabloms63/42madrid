/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   max.c                                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pmarcos- <pmarcos-@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/28 17:39:43 by pmarcos-          #+#    #+#             */
/*   Updated: 2026/01/28 17:49:23 by pmarcos-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>

int	max(int *tab, unsigned int len)
{
	int	num;
	int	cnt;

	cnt = 0;
	num = tab[0];
	while (cnt < len)
	{
		if (tab[cnt] > num)
			num = tab[cnt];
		cnt++;
	}
	return (num);
}

int	main(void)
{
	int	nums[6] = {0, 1, 2, 3, 4, -5};
	int cnt = 0;

	while (cnt < 6)
	{
		printf("%d\n", nums[cnt]);
		cnt++;
	}
	printf("%d\n", max(nums, 6));
	return (0);
}
