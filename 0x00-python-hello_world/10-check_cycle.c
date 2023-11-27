
#include "lists.h"
#include <stddef.h>


/**
 * check_cycle - Checks if a singly-linked list contains a cycle.
 * @list: A singly-linked list.
 *
 * Return: If there is no cycle - 0.
 *         If there is a cycle - 1.
 */
 int check_cycle(listint_t *list)
 {
 listint_t *up, *down;

	if (list == NULL || list->next == NULL)
	   	 return (0);

	up = list->next;
	down = list->next->next;

	while (up && down && down->next)
	 {
		if (up == down)
		   return (1);

		up = up->next;
		down = down->next->next;

		
	}

		return (0);
}
