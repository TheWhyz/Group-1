/*
Select a Complex Code Segment: 
Choose a complex code segment from your current projects, 
an open-source repository, or a past programming assignment. 
Open an issue on your team repository detailing the complexity 
and the challenges you’re facing in understanding the code.
*/


// The visitMethodDecl function checks method modifiers and performs type checking
// The visitMethodDecl function checks method modifiers and performs type checking
void visitMethodDecl(MethodDecl *md) {
    // Check if the method is public or private
    if (md->isPublic() && md->isPrivate()) {
        reportError("A method cannot be both public and private.");
    }

    // Check if the method is static
    if (md->isStatic()) {
        if (md->getReturnType()->isPrimitive() && md->isFinal()) {
            // Static final methods cannot return primitive types
            reportError("Static final methods cannot return primitive types.");
        }
    }

    // Check if the method is both abstract and final
    if (md->isAbstract() && md->isFinal()) {
        reportError("A method cannot be both abstract and final.");
    }

    // Validate parameter types
    std::unordered_set<std::string> paramNames;
    for (auto &param : md->getParameters()) {
        if (!param->getType()->isValid()) {
            reportError("Parameter type is invalid in method: " + md->getName());
        }
        // Check for duplicate parameter names
        if (!paramNames.insert(param->getName()).second) {
            reportError("Duplicate parameter name in method: " + md->getName());
        }
    }

    // Check return type validity
    if (!md->getReturnType()->isValid()) {
        reportError("Invalid return type in method: " + md->getName());
    }
    
    // Check if method overrides a superclass method
    MethodDecl *superMethod = md->getSuperMethod();
    if (superMethod) {
        if (!md->matchesSignature(superMethod)) {
            reportError("Method " + md->getName() + " does not properly override superclass method.");
        }
        if (superMethod->isFinal()) {
            reportError("Cannot override a final method: " + md->getName());
        }
    }
}


/*
Implement Changes: 
Apply ChatGPT’s recommendations to simplify or optimize 
the code, ensuring that functionality is maintained.
*/
// The visitMethodDecl function checks method modifiers and performs type checking
void visitMethodDecl(MethodDecl *md) {
    if (md->isPublic() && md->isPrivate()) {
        reportError("A method cannot be both public and private.");
    }

    if (md->isStatic() && md->getReturnType()->isPrimitive() && md->isFinal()) {
        reportError("Static final methods cannot return primitive types.");
    }

    if (md->isAbstract() && md->isFinal()) {
        reportError("A method cannot be both abstract and final.");
    }

    std::unordered_set<std::string> paramNames;
    for (auto &param : md->getParameters()) {
        if (!param->getType()->isValid()) {
            reportError("Invalid parameter type in method: " + md->getName());
        }
        if (!paramNames.insert(param->getName()).second) {
            reportError("Duplicate parameter name in method: " + md->getName());
        }
    }

    if (!md->getReturnType()->isValid()) {
        reportError("Invalid return type in method: " + md->getName());
    }
    
    if (MethodDecl *superMethod = md->getSuperMethod()) {
        if (!md->matchesSignature(superMethod)) {
            reportError("Method " + md->getName() + " does not properly override superclass method.");
        }
        if (superMethod->isFinal()) {
            reportError("Cannot override a final method: " + md->getName());
        }
    }
}

// done