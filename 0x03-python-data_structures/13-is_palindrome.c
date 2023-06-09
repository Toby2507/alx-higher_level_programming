#include "lists.h"

/**
 * reverse_list - Reverses a linked list
 * @head: head of the linked list
 *
 * Return: pointer to the reversed list
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL, *curr = head, *next;

	while (curr != NULL)
	{
		next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;
	}
	return (prev);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: head of the linked list
 *
 * Return: 0 on success and 1 on failure
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *prev, *second_half, *midnode;
	int is_palindrome = 1;

	if (*head == NULL || (*head)->next == NULL)
		return (is_palindrome);
	slow = *head;
	fast = *head;
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev = slow;
		slow = slow->next;
	}
	if (fast != NULL)
	{
		midnode = slow;
		slow = slow->next;
	}
	second_half = slow;
	prev->next = NULL;
	second_half = reverse_list(second_half);
	while (*head && second_half)
	{
		if ((*head)->n != second_half->n)
		{
			is_palindrome = 0;
			break;
		}
		*head = (*head)->next;
		second_half = second_half->next;
	}
	second_half = reverse_list(second_half);
	if (midnode)
	{
		prev->next = midnode;
		midnode->next = second_half;
	}
	else
		prev->next = second_half;
	return (is_palindrome);
}
