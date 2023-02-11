% Generate 3 independent vectors
vectors = rand(3, 5);

% Orthonormalize the vectors using the Gram-Schmidt process
[orthonormal_vectors, ~] = qr(vectors, 0);

% Print the original vectors
disp('Original vectors:');
disp(vectors);

% Print the orthonormal vectors
disp('Orthonormal vectors:');
disp(orthonormal_vectors);



