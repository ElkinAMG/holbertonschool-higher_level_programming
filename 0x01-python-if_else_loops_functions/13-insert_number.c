#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - insert a new node in ordened way.
 * @head: Linked list's head.
 * @number: Number to add within.
 *
 * Return: It returns the address to the new node, on failure NULL.
 */

listint_t *insert_node(listint_t **head, int number)
{
	int flag = 0;
	listint_t *current, *post, *newNode;

	if (!head)
		return (NULL);

	if (*head)
		post = *head, current = post;
	else
		post = NULL, current = NULL;

	newNode = malloc(sizeof(listint_t));
	if (!newNode)
		return (NULL);

	newNode->n = number;

	if ((post != NULL && (number < post->n)) || !(*head))
		newNode->next = *head, *head = newNode, flag = 1;

	while (post && flag == 0)
	{
		if (number < post->n)
		{
			newNode->next = post, current->next = newNode;
			break;
		}

		current = post, post = post->next;
	}

	if ((!post && flag == 0))
		current->next = newNode, newNode->next = NULL;

	return (newNode);
}
