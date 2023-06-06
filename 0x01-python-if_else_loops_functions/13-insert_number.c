#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: linked list head
 * @number: new number to be inserted
 *
 * Return: address of the new node, NULL on failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *curr, *prev, *new_node;

	new_node = malloc(sizeof(listint_t));
	if (!new_node || !head)
		return (NULL);
	curr = *head;
	new_node->n = number;
	new_node->next = NULL;
	if (!(*head) || number <= (*head)->n)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	curr = *head;
	prev = NULL;
	while (curr && number > curr->n)
	{
		prev = curr;
		curr = curr->next;
	}
	prev->next = new_node;
	new_node->next = curr;
	return (new_node);
}
