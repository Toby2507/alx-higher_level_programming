#include "lists.h"

/**
 * rev_list - Reverses a linked list
 * @head: head of the linked list
 */
void rev_list(listint_t **head)
{
	listint_t *prev = NULL, *curr = *head, *next;

	while (curr != NULL)
	{
		next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;
	}
	*head = prev;
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: head of the linked list
 *
 * Return: 0 on success and 1 on failure
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *second_half = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (fast && fast->next)
	{
		fast = fast->next->next;
		slow = slow->next;
	}
	second_half = fast ? slow->next : slow;
	rev_list(&second_half);
	slow = *head;
	while (slow && second_half)
	{
		if (slow->n != second_half->n)
			return (0);
		slow = slow->next;
		second_half = second_half->next;
	}
	return (1);
}
