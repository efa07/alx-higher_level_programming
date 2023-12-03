#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: head of the linke list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
	{
		return (1);
	}
	listint_t *slow_ptr = *head;
	listint_t *fast_ptr = *head;

	while (fast_ptr->next != NULL && fast_ptr->next->next != NULL)
	{
		slow_ptr = slow_ptr->next;
		fast_ptr = fast_ptr->next->next;
	}
	listint_t *prev = NULL;
	listint_t *curr = slow_ptr->next;
	listint_t *next = NULL;

	while (curr != NULL)
	{
		next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;
	}
	listint_t *left = *head;
	listint_t *right = prev;

	while (right != NULL)
	{
		if (left->n != right->n)
		{
			return (0);
		}
		left = left->next;
		right = right->next;
	}
	return (1);
}
